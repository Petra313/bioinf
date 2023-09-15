with open('mass.txt', 'r') as f:
  lines = [line.strip().split(':') for line in f.readlines()]
def get_mass():
  G = {}
  for pair in lines:
    G[pair[0]] = int(pair[1])
  return G

def findSpectrum(peptide):
  n = len(peptide) # n je duljina peptida
  mass = get_mass() # radimo kopiju masa aminokiselina
  # produlji peptid kopijom peptid do predzadnjeg znaka
  extended_peptide = peptide + peptide[:-2]  # jer je ciklicni peptid
  spectrum = [] # spektar masa
  spectrum.append(0) # dodaj pocetnu nulu
  # zbroji mase iz rijecnika za svako slovo u peptidu
  # i dodaj u spektar
  spectrum.append(sum([mass[x] for x in peptide]))
  # dvi petlje kako bi dobili sve kombinacije peptida
  for l in range(n): # za svako slovo u peptidu
    for k in range(1, n): # za svako slovo u peptidu od 1 do n
      subpeptide = extended_peptide[l : l + k] # uzmi subpeptid od l do l+k
      # u spektar dodaj sumu mase za subpeptid
      spectrum.append(sum([mass[x] for x in subpeptide]))
  return sorted(spectrum) # vrati sortirani spektar
     

# slican score-u iz BA4G
def score(peptide, spectrum_):
  pep_spec = findSpectrum(peptide) # teoretski spektar ciklopeptida
  result = 0 # postavi rezultat na 0
  # jedinstvene mase su skup (brojevi se ne ponavljaju)
  # teoretskog spektra i dobivenog spektra
  unique_masses = set(pep_spec + spectrum_)
  for mass in unique_masses: # za svaku masu u jedinstvenim masama
    # u rezultat pribroji -> prebroji pojavljivanja u teoretskom spektru
    # ciklopeptida i dobivenom spektru te izmedu ta dva odaberi minimalni
    # broj pojavljivanja
    result += min(pep_spec.count(mass), spectrum_.count(mass))
  return result # vrati rezultat


with open("rosalind_ba4f.txt", "r") as f:
  peptide = f.readline().strip()
  spect = f.readline().split()
spectrum_ = [int(x) for x in spect]
print(score(peptide, spectrum_))
