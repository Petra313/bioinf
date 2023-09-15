def chromosome_to_cycle(chromosome, external = True):
  nodes = []
  # petlja prolazi kroz svaki blok (segment) u kromosomu
  for block in chromosome:
    if block > 0: # ako je blok veci od 0
      # dodaj p[i], p[i+1]
      nodes.append(2 * block - 1)
      nodes.append(2 * block)
    else: # inace
      # dodaj p[i+1], p[i]
      nodes.append(-2 * block)
      nodes.append(-2 * block - 1)
  if external:
    return nodes
  return '(' + ' '.join(str(x) for x in nodes) +')'

chrom = '(+1 -2 -3 +4)'
chromosome = chrom.replace("(", "").replace(")", "")
chromosome = [int(x) for x in chromosome.split()]
chromosome_to_cycle(chromosome)

def colored_edges(P):
  # prazna lista edges koja ce sadrzavati obojene bridove
  edges = list()
  # petlja prolazi kroz svaki kromosom u listi P
  for chromosome in P:
    # pretvara kromosom u ciklicki zapis i rezultat se sprema u listu nodes
    nodes = chromosome_to_cycle(chromosome, external = True) # BA6F
    # petlja prolazi kroz indekse j u koracima od 2, pocevsi od 1, sto znaci da
    # ce se uzeti u obzir svaki drugi element u listi nodes
    for j in range(1, len(nodes), 2):
      # provjerava se je li indeks j razlicit od broja elemenata u listi nodes
      # umanjenog za 1 - ova provjera se vrsi kako bi se osiguralo da se
      # posljednji brid ne dodaje posebno jer je povezan s pocetnim cvorom
      if j != len(nodes) - 1:
        # ako uvjet iz prethodne linije nije ispunjen, dodaje se brid u listu
        # edges koji je oblikovan kao lista s dva cvora, nodes[j] i nodes[j + 1]
        edges.append((nodes[j], nodes[j + 1]))
      # inace, j je jednak broju elemenata u listi nodes umanjenom za 1
      # sto znaci da se radi o posljednjem bridu
      else:
        # dodaje se posljednji brid u listu edges koji je oblikovan kao lista s
        # dva cvora, nodes[j] i pocetnim cvorom nodes[0]
        edges.append((nodes[j], nodes[0]))
  # na kraju funkcija vraca listu edges koja sadrzi obojene bridove
  return ' '.join(str(x) for x in edges)

P = '(+1 -2 -3)(+4 +5 -6)'
P = P[1:-1] # uklanjamo vanjske zagrade
P = P.split(')(') # razdvajamo po unutarnjim zagradama
# pisemo zasebno elemente i pretvaramo u brojeve
for i in range(len(P)):
  P[i] = [int(x) for x in P[i].split(' ')]
result = colored_edges(P)
     

with open("rosalind_ba6h (1).txt", "r", encoding='utf-8') as f:
  inline = f.readline().strip()
P = inline[1:-1] # uklanjamo vanjske zagrade
P = P.split(')(') # razdvajamo po unutarnjim zagradama
# pisemo zasebno elemente i pretvaramo u brojeve
for i in range(len(P)):
  P[i] = [int(x) for x in P[i].split(' ')]
result = colored_edges(P)
print(result)

