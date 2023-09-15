
from math import inf
from copy import deepcopy
from collections import defaultdict
from math import floor # zaokruzivanje
from itertools import product # komb

def parse_graph(graph):
  g = defaultdict(list) # rjecnik koji stvara praznu listu kada ne pronade kljuc
  for x in graph: # za svaki element iz liste iz ulaznog grafa
    n, o = x.split("->") # n je kljuc (prije strelice), o su vrijednosti iza
    # vrijednosti rastavi na cvor sa svojom vrijednosti
    node, weight = o.split(":")
    # nadodaj kljucu ako postoji, ako ne postoji stvara se novi,
    # u listu vrijednosti gdje je vrijednost rjecnik za n cvor i za w tezinu
    g[n] += [{"n": node, "w": int(weight)}]
  return g # vrati graf (rjecnik)
     

# incoming prima graf kao ulazni argument i stvara "obrnuti" graf
# sto su do sada bili kljucevi, sada postaju vrijednosti, a vrijednosti kljucevi
def incoming(graph):
  x = defaultdict(list) # rjecnik koji predstavlja obrnuti graf
  k = list(graph.keys()) # lista kljuceva grafa
  # na listu kljuceva iz grafa nadodaj cvorove iz vrijednosti
  k += [x["n"] for v in graph.values() for x in v]
  for g in list(set(k)): # za svaki ne duplicirani cvor iz liste cvorova
    for node in graph[g]:
      # postavi kao kljuc cvor iz vrijednosti rjecnika grafa, a
      # vrijednosti uz originalnu tezinu, cvor iz neponavljajucih kljuceva
      x[node["n"]] += [{"n": g, "w": node["w"]}]
  return x
     

# cvorovi koji nemaju rubove koji vode do njih
def sources(graph):
  inc = incoming(graph) # preokreni graf
  # vrati listu elemenata ako nemaju vrijednosti u grafu
  return [g for g in graph if len(inc[g]) == 0]
     

def topological_order(graph):
  graph = deepcopy(graph) # stvori duboku kopiju niza
  order = [] # redosljed lista
  candidates = sources(graph) # prvi kandidat u grafu
  while candidates: # dok ima kandidata
    n = candidates[0] # uzmi prvog s reda kandidata
    order.append(n) # nadodaj ga u niz
    candidates.remove(n) # ukloni kandidata iz kandidata
    graph[n] = [] # ukloni vrijednosti iz grafa za cvor n
    # kandidati su izvori koji ne postoje u skupu liste poretka
    candidates = list(set(sources(graph)) - set(order))
  return order # vrati poredak

     

# racuna najduzi put u usmjerenom grafu od izvora (src) do cilja (sink)
# prima graf, izvor i cilj
# dinamicko programiranje
def longest_path(graph, src, sink):
  src = str(src) # izvor pretvori u string
  sink = str(sink) # dubinu pretvori u string
  score = {} # rjecnik za spremanje rezultata
  # inicijalna vrijednost su prazne liste,
  # a sadrzavat ce putanje od izvora do svakog cvora u grafu.
  path = defaultdict(list) # put
  for node in graph: # za svaki cvor u grafu (kljuc u rjecniku)
    # postavi rezltat za cvor iz grafa na najmanju mogucu vrijednost
    score[node] = -inf
  # postavi da je rezultat od izvora 0
  # jer je duljina puta od izvora do izvora 0
  score[src] = 0
  path[src] = [src] # postavljanje pocetnog cvora putanje za izvor u path
  # kako bi se dobila veza od svakog cvora prema njegovim dolaznim cvorovima
  inc = incoming(graph) # obrni kljuceve i vrijendosti
  order = topological_order(graph) # vrati topoloksi redosljed
  # iterriraj po cvorovima u redosljedu od cvora nakon izvora pa do kraja
  for node in order[order.index(src) + 1 :]:
    if len(inc[node]): # ako se cvor veze s drugima
      # racunanje rezultata kao zbroj rezultata prethodnih
      # cvorova i tezina bridova koji vode prema trenutnom cvoru za svaki cvor
      scores = [score[pre["n"]] + pre["w"] for pre in inc[node]]
      # pronalazenje najveceg zbroja rezultata i
      # azuriranje rezultata za trenutni cvor
      score[node] = max(scores)
      # Pronalazenje indeksa najveceg zbroja rezultata
      i = scores.index(max(scores))
      # azuriranje putanje za trenutni cvor tako da se kopira putanja prethodnog
      # cvora (iz obrnutog grafa) i doda trenutni cvor na kraj putanje
      path[node] = path[inc[node][i]["n"]] + [node]
  # Vracanje rezultata najduzeg puta i putanje od izvora do cilja
  return score[sink], path[sink]

with open("rosalind_ba5d.txt", "r", encoding='utf-8') as f:
  lines = [line.rstrip() for line in f]
  source = int(lines[0])
  sink = int(lines[1])
  graph = lines[2:len(lines)]
score, path = longest_path(parse_graph(graph), source, sink)
print(score)
print(*path, sep="->")