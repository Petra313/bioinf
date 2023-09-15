from copy import deepcopy
from collections import defaultdict
from math import floor # zaokruzivanje
from itertools import product # komb

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
     

def parse_graph(graph):
  # inicijalizacija praznog rjecnika
  # ovo osigurava da ce se za svaki cvor automatski stvoriti prazna lista ako
  # cvor jos nije prisutan u grafu
  g = defaultdict(list)
  for edge in graph:
    # razdvaja brid na dva dijela
    # pocetni cvor i zavrsni cvorovi
    x, nodes = edge.split(" -> ")
    # za svaki cvor u zavrsnim cvorovima (sa zarezom)
    for y in nodes.split(","):
      # u rjecnik nadodaj ga kao cvor i tezinu do njega
      g[x] += [{"n": y, "w": 0}]
  # vrati rjecik (graf)
  return g
     


with open("rosalind_ba5n.txt", "r", encoding='utf-8') as f:
  graph = [line.rstrip() for line in f]
print(*topological_order(parse_graph(graph)), sep=", ")
     