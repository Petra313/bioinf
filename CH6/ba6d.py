
import re
from collections import defaultdict


def parse_genome_graph(s):
  g = defaultdict(list)
  # razdvaja komponente na temelju zatvorene zagrade
  # svaka pronadena komponenta se pretvara u listu brojeva pomocu
  # component.split() i map(int, ...)
  # komponenta je oblika "1 2 3" i pretvara se u listu [1, 2, 3]
  for component in re.findall(r"", s):
    component = list(map(int, component.split()))
    for i in range(len(component) - 1):
      # dodavanje suprotnog brida u graf - svi susjedi povezani
      g[component[i]] += [-component[i + 1]]
      g[-component[i + 1]] += [component[i]]
    # zadnjem cvoru dodaj nulti - ciklicnost
    g[component[-1]] += [-component[0]]
    g[-component[0]] += [component[-1]]
  return g

def find_component(node, graph, with_neg = False):
  q = [node] # dodaj pocetni cvor u listu za pretrazivanje
  if with_neg: visited = list()
  else: visited = set() # skup za spremanje posjecenih
  while q: # dok postoje elementi u q
    node = q.pop(0) # izbaci prvog iz liste
    if with_neg: visited.append(node)
    else: visited.add(node) # dodaj cvor u skup posjecenih
    for n in graph[node]: # dok postoje susjedni cvorovi cvora
      if with_neg: n = -n
      if n not in visited: # ako cvor nije u posjecenima
        q += [n] # dodaj cvor u listu za pretrazivanje
  return visited # vrati sve posjecene cvorove
     
def breakpoint_graph(p, q):
  bg = {}
  for node in p.keys():
    bg[node] = p[node] + q[node]
  # vraca rezultirajuci graf bg koji predstavlja spojene razlomne tocke
  return bg

# uzima listu perm kao ulazni argument i vraca formatiranu verziju te liste
# input:  [1, -2, 3, 0]
# output (+1 -2 +3 +0)
def format_perm(perm):
  # f"{x:+}" - predznak
  return "(" + " ".join([f"{x:+}" for x in perm]) + ")"
     

def find_connected_components(graph):
  nodes = set(graph.keys()) # skup cvorova u grafu
  while nodes: # dok ima cvorova
    # pronadi komponente za svaki cvor
    res = find_component(next(iter(nodes)), graph) #BA6C
    nodes = nodes - res # ukloni iz cvorova za pretragu one koji su istrazeno
    # vrati povezane komponente u svakom koraku
    yield res
     

# nebanalni ciklusi - jednostavni ciklusi - barem 3 cvora i ne prolazi istim
# bridom vise od jednom
def non_trivial_cycle_nodes(graph):
  # za svaku povezanu komponentu
  for c in find_connected_components(graph): # BA6C
    # ako je ciklus nebanalan
    if len(c) > 2:
      # vrati povezanu komponentu
      return list(c)
  # nema nebanalinh ciklusa
  return None
     

def format_genome_graph(g):
  nodes = set(g.keys()) # skup cvorova
  components = [] # komponente
  # izvrsava se sve dok ima cvorova u skupu nodes
  while nodes:
    # uzmi sve komp koje krecu od cvora
    comp = find_component(next(iter(nodes)), g, with_neg = True)
    nodes = nodes - set(comp) # smanji cvorove za pretragu s prijedenim
    nodes = nodes - set(-x for x in comp) # ukloni one i suprotnog predznaka
    components += [comp] # u komponente dodaj novopronadenu komponentnu
  # formatiraj svaku komponentu za ispis
  x = [format_perm(c) for c in components]
  return "".join(x)
     

def add_edge(g, i, j): # dodavanje bridova izmedu cvorova
  g[i] += [j]
  g[j] += [i]
def del_edge(g, i, j): # uklanjanje bridova izmedu cvorova
  g[i].remove(j)
  g[j].remove(i)
     

# koristi se za izracunavanje najkraceg transformacijskog puta izmedu dvaju
# genoma P i Q - petlja se izvrsava sve dok postoji nebanalni ciklus u grafu
# a svaki put kad se izmijene bridovi u grafu P - generira se formatirana
# verzija trenutnog grafa
def shortest_transform(P, Q):
  # napravi graf razlomnih tocaka iz permutacija P i Q
  bg = breakpoint_graph(P, Q) # BA6C
  # pronadi sve netrivijalne cikluse u grafu razlomnih tocaka
  nodes = non_trivial_cycle_nodes(bg)
  # vrati perm P kao prvi korak
  yield format_genome_graph(P) # (+1 -2 -3 +4)
  #  izvrsava sve dok ima cvorova u varijabli nodes
  while nodes:
    # j se postavlja na prvi cvor u nodes - ovaj cvor predstavlja proizvoljni
    # brid iz q bridova u nebanalnom ciklusu
    j = nodes[0]
    # i2 se postavlja na prvi cvor u Q koji je povezan s cvorom nodes[0]
    # ovaj cvor predstavlja brid iz referentnih bridova koji je povezan
    # s cvorom j
    i2 = Q[nodes[0]][0]
    # postavlja se na prvi cvor u P koji je povezan s cvorom j
    # cvor predstavlja brid iz referentnih bridova koji je povezan s cvorom j
    i = P[j][0]
    # j2 se postavlja na prvi cvor u P koji je povezan s cvorom i2
    # cvor predstavlja brid iz referentnih bridova koji je povezan s cvorom i2
    j2 = P[i2][0]
    # ukloni postojece veze
    del_edge(P, i, j)
    del_edge(P, i2, j2)
    # dodaj nove veze - prespoji
    add_edge(P, j, i2)
    add_edge(P, j2, i)
    # vrati novo stanje
    yield format_genome_graph(P)
    # azuriraj stanje
    bg = breakpoint_graph(P, Q)
    nodes = non_trivial_cycle_nodes(bg)

P = '(+1 -2 -3 +4)'
Q = '(+1 +2 -4 -3)'
for g in shortest_transform(parse_genome_graph(P), parse_genome_graph(Q)):
  print(g)
     
(+1 -2 -3 +4)
(+1 +2 -3 +4)
(+1 +2 -4 +3)
(+1 +2 -4 -3)

with open("rosalind_ba6d.txt", "r", encoding='utf-8') as f:
  P, Q = [x.strip("\n") for x in f.readlines()]
for g in shortest_transform(parse_genome_graph(P), parse_genome_graph(Q)):
  print(g)
     