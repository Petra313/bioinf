
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
     

def insert_indel(word, i):
  return word[:i] + "-" + word[i:]
     

def addDirection(x, y, m, px, py, pm, i, j, v, w, epsilon, sigma):
  # rjecnik - sadrzi vrijednosti kazni ili nagrada za odredene parove znakova
  score = Scores
  # s je jednak 2 elementa, gornjem iz x - epsilon
  # i gornjem iz m - sigma
  s = [x[i - 1, j] + epsilon, m[i - 1, j] + sigma]
  x[i, j] = max(s) # x na trenutnoj poziciji je maksimum izmedu 2 matrice
  # u px spremi je li vodi do tog elementa x ili m
  px[i, j] = s.index(x[i, j])
  # s je jednak 2 elementa, lijevom iz x - epsilon
  # i lijevom iz m - sigma
  s = [y[i, j - 1] + epsilon, m[i, j - 1] + sigma]
  y[i, j] = max(s) # trazi se maskimum iz s i postavlja u y na trenutnu poz
  # u py spremi je li vodi do tog elementa y ili m
  py[i, j] = s.index(y[i, j])
  # s sadrzi tri elementa, vrijednost x i y na trenutnoj poziciji
  # te m na poziciji gore lijevo (dijagonalno) + vrijednost iz score
  # za odredena slova (na odredenoj poziciji -1 -> indeksiranje)
  s = [x[i, j], m[i - 1, j - 1] + score[v[i - 1]][w[j - 1]], y[i, j]]
  m[i, j] = max(s) # trazi se maksimum iz s i postavlja u m na trenutnu poz
  # u pm spremi je li vodi do tog elementa x ili m ili y
  pm[i, j] = s.index(m[i, j])
  return x, y, m, px, py, pm
     

def getWords(a1, a2, px, py, pm, i, j, s):
  while i * j != 0: # dok je umnozak razlicit od 0
   if s == 0: # ako je index scora nula (iz x)
     if px[i, j] == 1: # ako je na px na poziciji i,j postavljena vrijednost 1
       s = 1 # postavi s na 1
     i -= 1 # smanji index i za 1
     a2 = insert_indel(a2, j) # umetni prazninu na poziciji j u 2. stringu
   elif s == 1: # ako je index scora 1 (iz m)
     if pm[i, j] == 1: # i ako je na pm na poziciji i,j postavljena vrijednost 1
       i -= 1 # smanji i za 1
       j -= 1 # smanji j za 1
     else: # inace
       s = pm[i, j] # s postavi na vrijednost iz pm na pozciji i,j
   else: # inace
     if py[i, j] == 1: # ako je na py na poziciji i,j postavljena vrijednos 1
       s = 1 # postavi s na 1
     j -= 1 # smanji index od j
     a1 = insert_indel(a1, i) # u prvom stringu umetni prazninu na poziciju i
  # ako i ili j ostanu da su veci od 0, toliko crtica umetni na pocetak
  # kako bi se duzine izjednacile
  for _ in range(i):
    a2 = insert_indel(a2, 0)
  for _ in range(j):
    a1 = insert_indel(a1, 0)
  return a1, a2
     

# epsilon - prosirenje praznine
# sigma - otvaranje praznine
def global_affine(v, w, sigma=-11, epsilon=-1):
  # m sadrzi scores za poravnanje dijagonalno
  # x sadrzi scores za poravnanje prema gore
  # y sadrzi scores za poravnanje prema lijevo
  m, x, y = {}, {}, {}
  # rjecnik pm, px, py cuva indekse na koji element matrice m, x, y
  # je doprinjeo maksimalnom skoru u trenutnoj poziciji (i, j)
  px, pm, py = {}, {}, {}
  # postavi prvi lijevi na nulu u sve tri matrice
  x[0, 0], m[0, 0], y[0, 0] = 0, 0, 0
  # u cijeli prvi stupac postavi
  for i in range(1, len(v) + 1): # u duljini prve rijeci +1
    # kaznjavamo kako bi svaki sljedeci element imao vecu kaznu od prethonog
    # otvaranje praznine, prosirenje praznine i pomicanje
    x[i, 0] = sigma + (i - 1) * epsilon
    m[i, 0] = sigma + (i - 1) * epsilon
    # kako bi se stavila velika kazna
    y[i, 0] = 10 * sigma
  # u cijeli prvi redak postavi
  for j in range(1, len(w) + 1):
    # kaznjavamo kako bi svaki sljedeci element imao vecu kaznu od prethonog
    # otvaranje praznine, prosirenje praznine i pomicanje
    y[0, j] = sigma + (j - 1) * epsilon
    m[0, j] = sigma + (j - 1) * epsilon
    # kako bi se stavila velika kazna
    x[0, j] = 10 * sigma
  # iteriraj po matrici od prvog reda i stupca (nulti popunjeni)
  for i in range(1, len(v) + 1):
    for j in range(1, len(w) + 1):
      x, y, m, px, py, pm = addDirection(x, y, m, px, py, pm, i,
                                         j, v, w, epsilon, sigma)
  i, j = len(v), len(w) # i i j su duzine stringova
  a1, a2 = v, w # za sada su a1 i a2 pocetni stringovi
  scores = [x[i, j], m[i, j], y[i, j]] # pronadi scorove u donjem desnom rubu
  max_score = max(scores) # pronadi maksimum izmedu tih scores
  s = scores.index(max_score) # uzmi index najveceg da znamo iz koje je matrice
  a1, a2 = getWords(a1, a2, px, py, pm, i, j, s)
  # vrati maksimalan dobiveni score , poravnate stringove a1 i a2
  return max_score, a1, a2


with open("rosalind_ba5j.txt", "r", encoding='utf-8') as f:
  inlines = [x.strip("\n") for x in f.readlines()]
  first_word, second_word = inlines

print(*global_affine(first_word, second_word), sep='\n')