
from math import floor # zaokruzivanje

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
     


# prima prvu i drugu rijec, matrica skorova koja sadrzi vrijednosti kazni
# ili nagrada za odgovarajuce parove znakova te
# kaznu za otvaranje praznine ili prosirenje praznine u poravnanju
def calculate_scores(s1, s2, scores, penalty):
  # sc se inicijalizira kao lista duljine n+1 s vrijednostima od 0 do
  # (n+1)*penalty s korakom penalty, ovo predstavlja kazne za otvaranje praznine
  # na svakoj poziciji u prvom redu matrice poravnanja
  sc = list(range(0, (len(s1) + 1) * penalty, penalty))
  # postavi sve vrijednosti nula u niz bt duljine prvog stringa + 1
  bt = [0] * (len(s1) + 1)
  for j in range(1, len(s2) + 1):
    # stvara se privremena kopija liste sc pod nazivom psc koja sadrzi
    # prethodne skorove za stupac
    psc = sc[:]
    # prvi element u novom stupcu sc postavlja se kao prethodni prvi element
    # (psc[0]) plus kazna penalty, sto predstavlja kaznu za otvaranje praznine
    sc[0] = psc[0] + penalty
    # iterira po prvom nizu (s1) od prvog do zadnjeg elementa
    for i in range(1, len(s1) + 1):
      # prvi element u opt je prethodni skor (psc[i]) plus kazna penalty
      # sto predstavlja kaznu za proširenje praznine.
      # drugi element u opt je skor iz prethodne pozicije u trenutnom stupcu
      # (sc[i-1]) plus kazna penalty
      # treci u opt je prethodni skor na dijagonalnoj poziciji (psc[i-1])
      # plus skor iz matrice skorova za par znakova s1[i-1] i s2[j-1]
      opt = [
          # vertikalno prosirenje praznine.
          psc[i] + penalty,
          # horiznontalno prosirenje praznine
          sc[i - 1] + penalty,
          # poravnanje znakova i dodaje skor iz matrice skorova
          psc[i - 1] + scores[s1[i - 1]][s2[j - 1]],
      ]
      sc[i] = max(opt) # pronadi maksimum izmedu troje navedenog
      bt[i] = opt.index(sc[i]) # spremi index tako da znamo odakle je doslo
  # lista skorova za svaki stupac u matrici poravnanja
  # lista povratnih putanja koja sadrzi informaciju o tome odakle je dosao
  # maksimalni skor za svaku poziciju u matrici poravnanja
  return sc, bt
     

# da bismo pronasli srednji rub, prvo pronalazimo najvecu bodovnu vrijednost
# srednji stupac, zatim pronadite rub od ovog cvora do sljedeceg.
# izracunava srednju bridnu tocku između dva niza znakova (s1 i s2)
# da bi se odredila optimalna pozicija za poravnanje dvaju stringova
def middle_edge(s1, s2, scores, penalty=-5):
  # srednja tocka mid kao polovica duljine stringa s2
  mid = floor((len(s2)) / 2)
  # racunanje skorova i pozicija najveceg za poravnanje prvog dijela niza s1
  # i prvog dijela niza s2 do srednje tocke mid
  # skorovi se pohranjuju u sc1
  sc1, _ = calculate_scores(s1, s2[:mid], scores, penalty)
  # racunanje skorova i pozicija najveceg za obrnuti drugi dio niza s1
  # i obrnuti drugi dio niza s2 od srednje tocke mid
  # skorovi se pohranjuju u sc1
  sc2, bt2 = calculate_scores(s1[::-1], s2[mid::][::-1], scores, penalty)
  # stvaraju se ukupni skorovi total zbrajanjem skorova iz sc1 i sc2
  # (obrnuta verzija), koristi se zip funkcija kako bi se iteriralo kroz skorove
  # iz sc1 i obrnutu verziju skorova iz sc2
  # te se zbrajaju na odgovarajucim pozicijama
  total = [a + b for (a, b) in zip(sc1, sc2[::-1])]
  # pronalazi indeks maksimalne vrijedosti iz total
  best = total.index(max(total))
  # stvara se tocka n1 s indeksom best i srednjom tockom mid
  n1 = (best, mid)
  # stvara se lista moves koja sadrzi tri moguca pomaka za poravnanje
  # ovisno o vrijednosti u pozicijama najvecih bt2
  # pomaci se odnose na promjene indeksa u matrici poravnanja
  moves = [(n1[0], n1[1] + 1), (n1[0] + 1, n1[1]), (n1[0] + 1, n1[1] + 1)]
  # stvara se tocka n2 na temelju odabranog pomaka iz moves
  # koristi se obrnuti redoslijed vrijednosti u povratnoj traci bt2
  n2 = moves[bt2[::-1][best]]
  # vracamo tocke
  return (n1, n2)



with open("rosalind_ba5k.txt", "r", encoding='utf-8') as f:
  inlines = [x.strip("\n") for x in f.readlines()]
  first_word, second_word = inlines

print(*middle_edge(first_word, second_word, Scores), sep=' ')
     