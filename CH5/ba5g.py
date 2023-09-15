
def edit_distance(s1, s2): # izracunava udaljenost izmedu s1 i s2
  m = {} # inicijalizira se prazan rjecnik m za pohranjivanje udaljenosti
  for j in range(len(s2) + 1): # u duljini stringa s2 + 1
    m[j, 0] = j # prvi stupac matrice popuni indeksima
  for i in range(len(s1) + 1): # u duljini stringa s1 + 1
    m[0, i] = i # prvi red matrice popuni indeksima
  # iteriranje po matrici gdje je j indeks reda, a i indeks stupca
  for j in range(len(s2)):
    for i in range(len(s1)):
       # ako se nalaze isti znakovi na poziciji i u s1 i pozicji j u s2
      if s1[i] == s2[j]:
        # ako su znakovi jednaki, to znaci da nema potrebe za promjenom
        # i kopira se prethodna minimalna udaljenost (od gore lijevo u matrici)
        # ova vrijednost predstavlja minimalnu udaljenost izmedu prefiksa
        # s1 duljine i + 1 i prefiksa s2 duljine j + 1
        m[j + 1, i + 1] = m[j, i]
      else: # inace, ako su razliciti
        # potrebna promjena i odabire se minimalna vrijednost iz tri
        # susjedna elementa u rjecniku - matrici m (lijevo, gore i gore-lijevo)
        # te se dodaje 1
        m[j + 1, i + 1] = min([m[j + 1, i], m[j, i], m[j, i + 1]]) + 1
  # kao rezultat vraca se vrijednost iz m na donjem desnom kutu, a ona
  # predstavlja ukupnu minimalnu udaljenost izmedu cijelog niza s1 i niza s2
  return m[len(s2), len(s1)]


with open("rosalind_ba5g.txt", "r", encoding='utf-8') as f:
  inlines = [x.strip("\n") for x in f.readlines()]
  first_word, second_word = inlines
print(edit_distance(first_word, second_word))
     