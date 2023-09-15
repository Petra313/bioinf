
def format_num(x):
  # x je svaki element
  if x >= 0: # ako je x veci ili jednak nula
    return f"+{x}" # dodaj plus ispred broja
  else: # inace
    return f"{x}" # ostavi broj kakav je
     
# pretvara ciklicki zapis u kromosomski zapis tako sto svaki par cvorova u
# ciklickom zapisu pretvara u jedan blok u kromosomu - ako je prvi cvor manji od
# drugog cvora, to predstavlja pozitivan blok, a ako je prvi cvor veci ili
# jednak drugom cvoru, to predstavlja negativni blok -
# funkcija vraca listu blokova kromosoma
def cycle_to_chromosome(nodes, external = False):
  chromosome = []
  for i in range(0, len(nodes), 2):
    if nodes[i] < nodes[i + 1]: # ako je p[i] < p[i+1] -> pozitivan predznak
      chromosome.append(nodes[i + 1] // 2)
    else: # ako je p[i] > p[i+1] -> negativan predznak
      chromosome.append(-nodes[i] // 2)
  if external:
    return chromosome
  return '(' + ' '.join([format_num(x) for x in chromosome]) + ')'


with open("rosalind_ba6g.txt", "r", encoding='utf-8') as f:
  inline = f.readline().strip()
nodes = inline.replace("(", "").replace(")", "")
nodes = [int(x) for x in nodes.split()]
print(cycle_to_chromosome(nodes))