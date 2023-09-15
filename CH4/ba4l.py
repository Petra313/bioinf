
with open('mass.txt', 'r') as f:
  lines = [line.strip().split(':') for line in f.readlines()]
def get_mass():
  G = {}
  for pair in lines:
    G[pair[0]] = int(pair[1])
  return G

def linearSpectrum(peptide, external = False):
  masses = get_mass() # dohvati mase
  spectrum = [0] # postavi nulu u spektar
  n = len(peptide) # dohvati duljinu peptida
  for i in range(n):
    for j in range(1, n-i+1):
      subpeptide = peptide[i: i+j] # uzmi subpeptide linearnog peptida
      # zbroji mase subpeptida i dodaj ih u spektar
      spectrum.append(sum([masses[x] for x in subpeptide]))
  spectrum.sort() # sortiraj spektar
  if external:
    return spectrum
  return ' '.join(str(x) for x in spectrum)

def linear_score(peptide, spectrum):
  # napravi linearni spektar peptida
  pep_spec = linearSpectrum(peptide, external = True)
  result = 0 # postavi rezultat na 0
  # pronadi sve jedinstvene mase u linearnom spektru i dobivenom spektru
  unique_masses = set(pep_spec + spectrum)
  for mass in unique_masses: # za svaku masu u jedinstvenim masama
    # dodaj (zbroji) minimum pojavljivanja odredene mase izmedu pojavljivanja
    # u linearnom spektru peptida i dobivenom spektru
    result += min(pep_spec.count(mass), spectrum.count(mass))
  return result # vrati rezultat
def LinearSpectrum(Peptide):
  mass_table = get_mass() # dohvati mase aminokiselina
  PrefixMass = [0] # postavi prefiks na niz koji sadrzi 0 -> uvijek krece s 0
  for i in range(len(Peptide)): # za svaki element u duljini peptida
    # na prefiks nadodaj masu peptida koji se nalazi na i-tom indeksu
    temp = PrefixMass[i] + mass_table[Peptide[i]]
    # nadodaj u listu temp
    PrefixMass.append(temp)
  linearSpectrum = [0]  # postavi linearni spektar na niz koji sadrzi 0
  for i in range(len(Peptide)): # za svaki element u peptidu
    # za svaki element u peptidu od i+1 pozicije
    for j in range(i + 1, len(Peptide) + 1):
      # nadodaj u linearni spektar razliku masa od i-tog i j-tog
      # elementa prefiks masa
      linearSpectrum.append(PrefixMass[j] - PrefixMass[i])
  linearSpectrum.sort() # sortiraj uzlazno
  return linearSpectrum # vrati linearni spektar
     
def linear_score(peptide, spectrum):
  pep_spec = LinearSpectrum(peptide) # napravi linearni spektar peptida
  result = 0 # postavi rezultat na 0
  # pronadi sve jedinstvene mase u linearnom spektru i dobivenom spektru
  unique_masses = set(pep_spec + spectrum)
  for mass in unique_masses: # za svaku masu u jedinstvenim masama
    # dodaj (zbroji) minimum pojavljivanja odredene mase izmedu pojavljivanja
    # u linearnom spektru peptida i dobivenom spektru
    result += min(pep_spec.count(mass), spectrum.count(mass))
  return result # vrati rezultat



def Trim(leaderboard, spectrum, N):
  if len(leaderboard) <= N: # ako je duzina ljestvice manja ili  jednaka N
    return leaderboard # vrati ljestvicu
  scores = {} # rijecnik postignuca
  # za svaku poziciju i i masu peptida u ljestvici
  for i, peptide in enumerate(leaderboard):
    # postavi index kao kljuc, a vrijednost linearnog Score-a peptida u spektru
    scores[i] = linear_score(peptide, spectrum)
  # napravi sortianu listu vrijednosti iz scores silazno
  sorted_scores = sorted(scores.values(), reverse=True)
  # postavi kao prag N-1-vi element iz sortiranih postignuca
  threshold = sorted_scores[N - 1]
  # vrati mase peptida iz ljestvice koji imaju veci score od praga
  # pronadi index, score iz originalne ljestvice unutar scores i
  # usporedi s granciom
  return " ".join([leaderboard[idx] for idx, score
          in scores.items() if score >= threshold])



with open("rosalind_ba4l.txt", "r") as f:
  leaderboard = f.readline().split()
  spect = f.readline().split()
  N = int(f.readline().strip())
spectrum_ = [int(x) for x in spect]
res = Trim(leaderboard, spectrum_, N)

print(res)