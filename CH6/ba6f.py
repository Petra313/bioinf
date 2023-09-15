
# pretvara kromosomski zapis u ciklicki zapis tako da svaki blok iz kromosoma
# pretvara u dva cvora u ciklickom zapisu - pozitivni blokovi se pretvaraju u
# dva cvora, jedan paran i jedan neparan, dok se negativni blokovi takoder
# pretvaraju u dva cvora, ali s promjenom znaka i redoslijeda brojeva - funkcija
# vraca listu cvorova ciklickog zapisa
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
     
[1, 2, 4, 3, 6, 5, 7, 8]

with open("rosalind_ba6f (1).txt", "r", encoding='utf-8') as f:
  inline = f.readline().strip()
chromosome = inline.replace("(", "").replace(")", "")
chromosome = [int(x) for x in chromosome.split()]
print(chromosome_to_cycle(chromosome))
     