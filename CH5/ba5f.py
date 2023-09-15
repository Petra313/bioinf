
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
     

def local_alignment(s1, s2, penalty=-5):
  # m - rjecnik koji predstavlja matricu bodova za poravnanje
  # kljucevi u rječniku su parovi (j, i) koji označavaju koordinatu u matrici
  # j je indeks za s2 (redak) i i indeks za s1 (stupac)
  # vrijednosti u rjecniku predstavljaju bodove za odredenu poziciju u matrici
  # p - rjecnik  koji predstavlja putanju u matrici bodova
  # kljucevi u rjecniku su isti parovi (j, i) kao u rjecniku m
  # a vrijednosti predstavljaju smjer kretanja pri izgradnji poravnanja
  m, p = {}, {}
  for j in range(len(s2) + 1): # u duzini drugog stringa (visina matrice) +1
    m[j, 0] = penalty * j # u nulti stupac postavi penale (-5, -10, -15...)
    p[j, 0] = "up" # u nulti stupac postavi da se mozemo samo popet
  for i in range(len(s1) + 1): # u duzini prvog stringa (sirina matrice) +1
    m[0, i] = penalty * i # u nulti red postavi penale (-5, -10, -15...)
    p[0, i] = "left" # u nulti red postavi da se samo mozemo kretat lijevo
  m[0, 0] = 0 # nulti element jednak je 0 (gornji lijevi kut)
  # U petljama for prolazimo kroz sve pozicije u matrici bodova,
  # osim pocetne pozicije.
  for j in range(len(s2)):
    for i in range(len(s1)):
      m, p = addDirection(m, p, j, i, s1, s2, penalty, scores_ = 2)  #BA5E
  # pronalazi najvecu vrijednost medu svim vrijednostima u rjecniku m
  max_score = max(x for x in m.values())
  # pronalazi kljuceve j i i u rjecniku m koji sadrze vrijednost max_score
  j, i = [k for k, v in m.items() if v == max_score][0]
  a1, a2 = getWords(p, m, s1, s2, j, i)
  # vrati najveci score, obrnute stringove a1 i a2
  return max_score, a1[::-1], a2[::-1]
     
def addDirection(m, p, j, i, s1, s2, penalty, scores_ = 1):
  # sadrzi vrijednosti kazni ili nagrada za odredene parove znakova
  if scores_ == 2:
    score = Scores2
  else:
    score = Scores # score je rjecnik
  new = (j + 1, i + 1) # trenutna pozicija u matrici (jer iskljucujemo 0,0)
  if scores_ == 2:
      opt = [
        # na trenutnu poziciju u matrici (rjecniku) bodovanja, nadodaj
        # penal iz rjecnika score za odredeni par
        m[j, i] + score[s1[i]][s2[j]], # dijagonalno
        m[j, i + 1] + penalty,  # od pozicije povise oduzmi penal (-5)
        m[j + 1, i] + penalty, # od pozicije lijevo oduzmi penal (-5)
        0
      ]
  else:
    opt = [
      # na trenutnu poziciju u matrici (rjecniku) bodovanja, nadodaj
      # penal iz rjecnika score za odredeni par
      m[j, i] + score[s1[i]][s2[j]], # dijagonalno
      m[j, i + 1] + penalty,  # od pozicije povise oduzmi penal (-5)
      m[j + 1, i] + penalty, # od pozicije lijevo oduzmi penal (-5)
    ]
  # pronadi maksimum za trenutnu poziciju od prijenavedenih - [-3, -15, -7]
  m[new] = max(opt)
  # ako je prvi index najveci u opt - onda je put do te tocke od gore-lijevo
  # ako je drugi index najveci u opt - onda je put do te tocke od gore
  # ako je treci index najveci u opt - onda je put do te tocke od lijevo
  if scores_ == 2:
    p[new] = ["diagonal", "up", "left", 'diagonal'][opt.index(max(opt))]
  else: p[new] = ["diagonal", "up", "left"][opt.index(max(opt))]
  return m, p
     
with open("rosalind_ba5f.txt", "r", encoding='utf-8') as f:
  inlines = [x.strip("\n") for x in f.readlines()]
  first_word, second_word = inlines
print(*local_alignment(first_word, second_word), sep="\n")
     