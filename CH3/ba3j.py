
from collections import Counter, defaultdict
import re
import ast

def prefix(a):
  return a[:-1]
def suffix(a):
  return a[1:]


def sortDict(D):
  graph = {}
  sorted= list(D.keys())
  sorted.sort()
  for key in sorted:
    graph[key] = D[key]
    graph[key].sort()
  return graph

 
def deBrujinFromKmers(kmers):
  D = {}
  for kmer in kmers:
    if prefix(kmer) not in D:
      D[prefix(kmer)] =[suffix(kmer)]
    else:
      D[prefix(kmer)].append(suffix(kmer))
      D[prefix(kmer)].sort()
  D = sortDict(D)
  res = []
  for key, value in D.items():
    res.append(key + ' -> ' + ','.join(value))
  return '\n'.join(res)

def getDict(directions):
  D = {} # rijecnik
  for direction in directions: # za svaku uputu
    # razdvoji na ono prije strelice i poslije
    first, second = direction.split(" -> ")
    # ako poslije strelice ima vise uputa, razdvoji
    second = second.split(",")
    D[first] = second # dodaj u rijecnik
  return D
    
def getACycle(graph, possible_starts):
  origin = None
  for start in possible_starts: # za svaki start u mogucim pocetcima
    if start in graph: # ako je start u grafu
      origin = start # postavi izvor na start
      break # prekini petlju
  if origin is None: # ako nema izvora -> iznimka
    raise
  cycle = []
  first = origin # postavi kao prvi izvor
  while True: # dok je istina
    if first in graph: # ako je prvi u grafu
      second = graph[first][0] # dohvati prvu vrijednost iz rijecnika za kljuc
      cycle.append([first, second]) # dodaj u ciklus par prvi-drugi
      if len(graph[first]) == 1: # ako je broj vrijednosti uz kljuc jednaka 1
        graph.pop(first, None) # izbaci kljuc
      else: # inace
        graph[first] = graph[first][1:] # ostavi samo element koji nije prijeden
      if second == origin: # ako je drugi jednak izvoru
        break # prekini petlju
      else:
        first = second # inace postavi prvog na drugog
    else: # inace, ako prvi nije u grafu
      break # prekini
  return cycle # vrati ciklus


def start_index(cycle, start):
  s_index = -1 # postavi s_index na neg. broj
  for i in range(0, len(cycle)): # za svaki element u ciklusu
    if cycle[i][0] == start: # ako je drugi element iz ciklusa jednak startu
      s_index = i # postavi index na i
      break # izadi iz petlje
  return s_index # vrati dobiveni index

def eulerianCycle(graph, start=None):
  graph = graph.copy() # napravi kopiju grafa
  cycles = []
  possible_starts = list(graph.keys())[:1] # postavi kao moguci pocetak prvi el
  if start != None: # ako je unesen start
    possible_starts = [str(start)] # broj koji cemo stavit za pocetak je uneseni
  while len(graph) > 0: # dok je duljina grafa veca od 0
    # vrati sve moguce krugove od moguceg pocetka
    new_cycle = getACycle(graph, possible_starts) # napravi novi ciklus
    # uzmi svaki prvi element iz novog ciklusa (u parovima)
    # i dodaj u listu mogucih pocetaka
    possible_starts.extend([x[0] for x in new_cycle])
    possible_starts = list(set(possible_starts)) # da se uklone duplikati
    cycles.append(new_cycle) # nadodaj novi ciklus
  if len(cycles) == 1: # ako je duzina ciklusa jednaka 1 (nije bilo grananja)
    # put je jedan niz (u dvostrukim je zagradama radi append u petlji)
    path = cycles[0]
  else: # inace
    path = cycles[0] # uzmi prvi dobiveni put
    for i in range(1, len(cycles)): # za svaki iduci ciklus
      next_ = cycles[i] # next je taj ciklus
      # pronadi index gdje cemo umetnit prvi element
      # ovog ciklusa u pocetni ciklus
      s_index = start_index(path, next_[0][0])
      # umetni element ovog ciklusa u pocetni ciklus
      path = path[:s_index] + next_ + path[s_index:]
  firsts = [str(x[0]) for x in path]
  firsts.append(str(path[-1][1]))
  return '->'.join(firsts)

def findEulerianPath(graph):
  graph, first, second = RebalanceGraphFromEulerianPathToCycle(graph)
  eulerCycle = eulerianCycle(graph) # napravi eulerov krug od dobivenog grafa
  path = eulerCycle[0:-1]
  parts = eulerCycle.split(f"{str(first)}->{str(second)}", maxsplit=1)
  if parts[0] == '':
    path = parts[1]
  elif parts[1] == '':
    path = parts[0]
  else:
    first = str(first)
    second = str(second)
    part1 = parts[0] + first
    part1_trim = part1.split('->', maxsplit = 1)[1]
    part2 = second + parts[1]
    path = part2 + '->' + part1_trim
  return path
     
def RebalanceGraphFromEulerianPathToCycle(graph):
  graph = graph.copy() # napravi kopiju grafa
  # broj vrijednosti za svaki kljuc
  outbalance = {first: len(graph[first]) for first in graph.keys()}
  new_list = []
  for v in graph.values(): # za svaku vrijednost u rijecniku
    new_list.extend(v) # nadodaj vrijednost u listu
  inbalance = Counter(new_list) # prebroji pojavljivanja svakog elementa
  # svi jedinstveni elementi koji se pojavljuju i u kljucevima i u vrijednostima
  all_nodes = set(list(outbalance.keys()) + list(inbalance.keys()))
  for node in all_nodes: # za svaki cvor u cvorovima
    # izracunaj razliku broja vrijednosti koje sadrzi
    # kljuc i broja pojavljivanja u vrijednostima
    balance = outbalance.get(node, 0) - inbalance.get(node, 0)
    if balance == 1: # ako je razlika jednaka jedan
      second = node # postavi drugi na taj cvor
    if balance == -1: # ako je razlika -1
      first = node # postavi prvi na cvor
  if first not in graph: # ako prvi nije u grafu u kljucevima
    # dodaj jos jednu vezu prvi - drugi (kljuc - vrijednost)
    graph[first] = [second]
  else: # inace
    # nadodaj drugi (vrijednost) na postojeci prvi (kljuc)
    graph[first].append(second)
  return graph, first, second # vrati graf, prvi i drugi


def getBinary(k):
  kmers = []
  for i in range(2**k):
    kmer = str(bin(i))[2:] # uzmi binarni zapis broja
    if len(kmer) < k:
      kmer = '0'*(k-len(kmer))+kmer # nadodaj nule na pocetak koje fale
    kmers.append(kmer)
  return kmers
def constructGraph(kmers):
  D = {}
  for kmer in kmers:
    if prefix(kmer) not in D: # prefix iz BA3C
      D[prefix(kmer)] = [suffix(kmer)]
    else:
      D[prefix(kmer)].append(suffix(kmer))
  return D

def kUniversalString(k):
  kmers = getBinary(k) #dohvati sve binarne zapise
  graph = constructGraph(kmers) # napravi debrujinov graf
  graph = sortDict(graph) # sortiaj
  cycle = eulerianCycle(graph) # napravi eulerov ciklus (BA3f)
  cycle = cycle.split('->')
  cycle = cycle[:len(cycle)-k+1] # uzmi do - (k-1) elementa
  res = cycle[0][:-1]
  for el in cycle:
    res += el[-1]
  return res



def pairedGraph(pairs):
  D= defaultdict(list)
  for pair in pairs:
    a1, a2 = pair.split('|')
    p1 = tuple([a1[:-1], a2[:-1]]) # napravi tuple od prefiksa 1. i 2. elementa
    p2 = tuple([a1[1:], a2[1:]]) # napravi tuple od sufiksa 1. i 2. elementa
    D[p1].append(p2) # dodaj u rjecnik
  return D

def stringFromPairedComposition(paired, k, d):
  path = findEulerianPath(paired) # pronadi eulerov put (BA3G)
  path = path.split('->') # napravu niz od puta
  path = [ast.literal_eval(x) for x in path] # stringove pretvori u tuples
  a1 = path[0][0][:-1]
  a2 = path[0][1][:-1]
  a1 += ''.join([x[0][-1] for x in path])
  a2 += ''.join([x[1][-1] for x in path])
  return a1+a2[-(k+d):]

with open("rosalind_ba3j.txt", "r") as f:
  k, d =f.readline().split()
  text = [line.strip() for line in f]

res = stringFromPairedComposition(pairedGraph(text), int(k), int(d))
print(res)
     