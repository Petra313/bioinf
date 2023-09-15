def addDirection(m, p, s1, s2, i, j, penalty = -1):
  new = (j + 1, i + 1) # trenutna pozicija u matrici (jer iskljucujemo 0,0)
  # postavi vrijednost na 1 ako je s1 na i-toj poziciji jednak s2 na j-toj
  # inace postavi na -1
  match_ = 1 if s1[i] == s2[j] else penalty
  opt = [
      m[j, i] + match_, # gornjem lijevom elementu dodaj match
      m[j, i + 1] + penalty, # gornjem dodaj penal
      m[j + 1, i] + penalty, # lijevom dodaj penal
  ]
  m[new] = max(opt) # na poziciji i+1 i j+1 u matrici je maksimum iz opt
  # pronad maksimum izmedu vrijednosti
  # gore-lijevo, gore i lijevo od elementa
  p[new] = ["diagonal", "up", "left"][opt.index(max(opt))]
  return m, p
     

def getWords(p, s1, s2, j, i):
  a1, a2 = '',''
  while i > 0 and j > 0: # dok su i *i* i *j* veci od 0
    if p[j, i] == "diagonal": # ako je na putu p na poziciji j,i up-left
      a1 += s1[i - 1] # uzmi prijasnji element od s1
      a2 += s2[j - 1] # uzmi prijasnji element od s2
      j, i = j - 1, i - 1 # samnji oba indeksa
    elif p[j, i] == "left": # ako je na putu p na poziciji j,i left
      a1 += s1[i - 1] # uzmi prijasnji element iz s1
      a2 += "-" # postavi na s2 crticu
      i = i - 1 # smanji indeks i za 1
    elif p[j, i] == "up": # ako jw na putu p na poziciji j, i up
      a1 += "-" # postavi na s1 -
      a2 += s2[j - 1] # uzmi prijasnji element iz s2
      j = j - 1 # smanji indeks j za 1
  return a1, a2
     

def fitting_alignment(s1, s2):
  # rjecnici - matrice za pohranjivanje vrijednosti, smjera
  m, p = {}, {}
  for j in range(len(s2) + 1): # za svaki element u stringu s2 +1
    m[j, 0] = -j # vrijednost u prvom stupcu matrice je negativan index
    p[j, 0] = "up" # u najlijevijem stupcu se samo moze ici prema gore
  for i in range(len(s1) + 1): # za svaki element u stringu s1 +1
    m[0, i] = 0 # vrojednost u prvom retku matrice su nule
    p[0, i] = "left" # u prvom retku matrice mozemo samo ici lijevo
  m[0, 0] = 0 # postavi 0,0 element matrice na 0
  # iteriraj po matrici gdje je j oznaka retka, a i stupca
  for j in range(len(s2)):
    for i in range(len(s1)):
      m, p = addDirection(m, p, s1, s2, i, j, penalty = -1)
  # zadnja vrijednost stupca u svakom retku
  sc = [m[len(s2), i] for i in range(len(s1) + 1)]
  max_score = max(sc) # pronadi maksimum u zadnjem retku
  i = sc.index(max_score) # index maksimuma (index stupca)
  j = len(s2) # j je velicina s2 - index retka
  a1, a2 = getWords(p, s1, s2, j, i)
  return max_score, a1[::-1], a2[::-1] # vrati maksimalni score, obrnute a1 i a2


with open("rosalind_ba5h.txt", "r", encoding='utf-8') as f:
  inlines = [x.strip("\n") for x in f.readlines()]
  first_word, second_word = inlines

print(*fitting_alignment(first_word, second_word), sep='\n')