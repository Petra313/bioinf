from itertools import product # komb



# provjerava je li pokazivac x valjan za trenutnu poziciju pos u matrici
# pokazivac je valjan ako se odnosi na nepozitivnu celiju u matrici, funkcija
# koristi prev(pos, x) da bi dobila prethodnu poziciju na temelju trenutne
# pozicije i pokazivaca, zatim provjerava je li svaki element u prethodnoj
# poziciji veci ili jednak nuli
# ako jesu, funkcija vraca True, inace vraca False
def valid_coord(x, pos):
  return all([i >= 0 for i in prev(pos, x)])
     

# dobiva prethodnu poziciju na temelju trenutne pozicije pos i pokazivaca ptr
# za svaki element na istoj poziciji u pos i ptr, zbraja ih i stvara tuple koji
# sadrzi rezultate
def prev(pos, ptr):
  return tuple([p + d for p, d in zip(pos, ptr)])
     

# racuna bodove (score) za odredeni polozaj i pokazivac
# za pokazivac (-1, -1, -1), funkcija provjerava jesu li svi simboli u trenutnom
# stupcu poravnanja jednaki, ako jesu, funkcija vraca 1, inace vraca 0
def score(seqs, pos, ptr):
  if ptr == (-1, -1, -1):
    bases = [seqs[i][j] for i, j in enumerate(prev(pos, ptr))]
    return all(x == bases[0] for x in bases)
  else:
    return 0
     

# generira moguce pomake (pokazivace) relativno na trenutnu celiju
# generira listu svih kombinacija pomaka za n broj dimenzija, gdje su moguci
# pomaci 0 i -1
# funkcija vraca sve kombinacije osim prvog, jer prva kombinacija (0, 0, ..., 0)
# predstavlja trenutnu poziciju i ne treba se uzeti u obzir
def moves(n):
  return list(product([0, -1], repeat=n))[1:]
     

# visestruko poravnanje (multiple alignment) nad stringovima iz seqs
def multiple_alignment(seqs):
  # m - rjecnik za pohranu bodova (score) za svaku poziciju u matrici poravnanja
  # p - rjecnik za pohranu pokazivaca koji vode do najveceg boda
  m, p = {}, {}
  m[0, 0, 0] = 0
  # definicija raspona za svaki string u seqs duljine odgovarajuceg stringa + 1
  ranges = [range(0, len(s) + 1) for s in seqs]
  # prolazimo kroz sve moguce pozicije
  for pos in product(*ranges):
   # filtriraju se valjani pokazivaci
   ptrs = list(filter(lambda x: valid_coord(x, pos), moves(3)))
   # ako nema valjanih pokazivaca
   if not len(ptrs):
       continue # preskace se korak i nastavlja se dalje
   # inace se racunaju bodovi (scores) za svaki valjani pokazivac
   sc = [m[prev(pos, x)] + score(seqs, pos, x) for x in ptrs]
   # najveci bod se sprema u m
   m[pos] = max(sc)
   # odgovarajuci pokazivac u p (indeks)
   p[pos] = ptrs[sc.index(max(sc))]
  # traceback to recover alignment
  # pohranjuje ukupan broj bodova
  tot = m[pos]
  # lista za pohranu poravnanja svakog stringa
  aln = ["", "", ""]
  # iteriramo po pozicijama sve dok imamo vrijednosti vece od nula
  while any([x > 0 for x in pos]):
    # dohvaca se odgovarajuci pokazivac za trenutnu poziciju
    ptr = p[pos]
    # za svaki element u nizu pocetnih stringova
    for i, seq in enumerate(seqs):
      # za odgovoarajuci string u nizu (nalazi se na poziciji i)
      # nadodaj slovo iz pocetnog niza na lokaciji pos[i] -1 (prijasnje)
      # ako je pokazivac -1 inace nadodaj -
      aln[i] += seq[pos[i] - 1] if ptr[i] == -1 else "-"
    # pozicija (pos) se azurira na prethodnu poziciju
    # To nam omogucava da se pomaknemo unatrag u matrici poravnanja
    pos = prev(pos, ptr)
  # vracamo ukupan broj bodova, kako smo isli od kraja obrnuta nova poravnanja
  # pocetnih stringova
  return tot, aln[0][::-1], aln[1][::-1], aln[2][::-1]

with open("rosalind_ba5m.txt", "r", encoding='utf-8') as f:
  inlines = [x.strip("\n") for x in f.readlines()]
print(*multiple_alignment(inlines), sep='\n')
     