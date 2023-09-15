    
fp = open("blosum62.scoring", "r")
scores = [x.strip("\n") for x in fp.readlines()] # razdvoji redove iz datoteke
Scores = {} # rjecnik
names = scores[0].split() # razdvoji prvi red sa samim slovima - niz
# za svaku liniju (element liste) od prvog elementa (prvi je names)
for line in scores[1:]:
  tmp = line.split() # razdvoji elemenete u liniji
  letter = tmp[0] # nulti element jer je slovo
  # sada od ostatka linije, pretvori ih u brojeve
  scoring = [int(x) for x in tmp[1:]]
  # u rjecnik za kljuc postavi slovo iz linije, a za vrijednosti
  # kombinaciju slova  iz names te score na poziciji iz scoring
  Scores[letter] = {k: v for k, v in zip(names, scoring)}
# Scores # matica za oznakama redaka kao kljucevima i stupaca u obliku rjecnika
     

fp2 = open("pam250.scoring", "r")
scores2 = [x.strip("\n") for x in fp2.readlines()] # razdvoji redove iz datoteke
Scores2 = {} # rjecnik
names2 = scores2[0].split() # razdvoji prvi red sa samim slovima - niz
# za svaku liniju (element liste) od prvog elementa (prvi je names)
for line in scores2[1:]:
  tmp = line.split() # razdvoji elemenete u liniji
  letter = tmp[0] # nulti element jer je slovo
  # sada od ostatka linije, pretvori ih u brojeve
  scoring = [int(x) for x in tmp[1:]]
  # u rjecnik za kljuc postavi slovo iz linije, a za vrijednosti
  # kombinaciju slova  iz names te score na poziciji iz scoring
  Scores2[letter] = {k: v for k, v in zip(names2, scoring)}
# Scores # matica za oznakama redaka kao kljucevima i stupaca u obliku rjecnika
     
def getWords(p, m, s1, s2, j, i):
  a1, a2 = "", "" # a1 i a2 su poravnati stringovi na kraju
  # krecemo od donjeg desnog kuta prema gornjem lijevom
  while i > 0 or j > 0: # dok su ili a ili j veci od nula
    if m[j, i] == 0: # ako je vrijednost jednaka 0 u rjecniku m
      break # prekini izvrsavanje
    if p[j, i] == "diagonal": # ako je na poziciji p[j, i] gore-lijevo
      a1 += s1[i - 1] # u string 1 nadodaj prijasnju poziciju pocetnog stringa1
      a2 += s2[j - 1] # u string 2 nadodaj prijasnju poziciju picetnog stringa2
      j, i = j - 1, i - 1 # umanji i *i* i *j*
    elif p[j, i] == "left": # ako je na poziciji p[j, i] lijevo
      a1 += s1[i - 1] # u string 1 nadodaj prijasnju poziciju pocetnog stringa1
      a2 += "-" # u string 2 nadodaj crticu
      i = i - 1 # smanji i
    elif p[j, i] == "up": # ako je na poziciji p[j, i] gore
      a1 += "-" # u string 1 nadodaj crticu
      a2 += s2[j - 1] # u string 2 nadodaj prijasnju poziciju pocetnog stringa2
      j = j - 1 # smanji j
  return a1, a2

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
     

def overlap_alignment(s1, s2, penalty=-2):
  # rjecnici - matrice za pohranjivanje vrijednosti, smjera
  m, p = {}, {}
  for j in range(len(s2) + 1): # za svaki element u stringu s2 +1
    m[j, 0] = j * penalty # vrijednost u prvom stupcu matrice je negativan index
    p[j, 0] = "up" # u najlijevijem stupcu se samo moze ici prema gore
  for i in range(len(s1) + 1): # za svaki element u stringu s1 +1
    m[0, i] = 0 # vrojednost u prvom retku matrice su nule
    p[0, i] = "left" # u prvom retku matrice mozemo samo ici lijevo
  m[0, 0] = 0 # postavi 0,0 element matrice na 0
  # iteriraj po matrici gdje je j oznaka retka, a i stupca
  for j in range(len(s2)):
    for i in range(len(s1)):
      m, p = addDirection(m, p, s1, s2, i, j, penalty) # BA5H
  # zadnja vrijednost retka u svakom u svakom stupcu
  sc = [m[j, len(s1)] for j in range(len(s2) + 1)]
  max_score = max(sc) # pronadi maksimum u zadnjem stupcu
  j = sc.index(max_score) # index maksimuma (index retka)
  i = len(s1) # i je velicina s1 - index retka
  a1, a2 = getWords(p, s1, s2, j, i) #BA5H
  return max_score, a1[::-1], a2[::-1] # vrati maksimalni score, obrnute a1 i a2


with open("rosalind_ba5i.txt", "r", encoding='utf-8') as f:
  inlines = [x.strip("\n") for x in f.readlines()]
  first_word, second_word = inlines

print(*overlap_alignment(first_word, second_word), sep='\n')
     