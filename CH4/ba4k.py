

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


with open("rosalind_ba4k.txt", "r") as f:
  peptide = f.readline().strip()
  spect = f.readline().split()
spectrum_ = [int(x) for x in spect]
res = linear_score(peptide, spectrum_)
print(res)