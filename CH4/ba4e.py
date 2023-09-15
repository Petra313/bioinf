
from collections import Counter, defaultdict



with open('mass.txt', 'r') as f:
  lines = [line.strip().split(':') for line in f.readlines()]
def get_mass():
  G = {}
  for pair in lines:
    G[pair[0]] = int(pair[1])
  return G

def cyclospectrum(peptide): # definicija ciklospektra
  n = len(peptide) # peptid duljine n
  mass = get_mass() # dohvatimo mase
  # prolazi i do  -2 -> abcd -> abcdab -> ciklicnost
  extended_peptide = peptide + peptide[:-1] # prosirimo peptid
  spectrum = [0, sum(peptide)] # u spektar dodamo nulu i cijelu sumu
  for l in range(n): # iteriramo po listi
    for k in range(1, n): # dujine peptida
      subpeptide = extended_peptide[l : l + k] # trazimo sve podpeptide
      spectrum.append(sum(subpeptide)) # dodajemo sumu u spektar
  return sorted(spectrum) # vracamo sortirani spektar

def linearspectrum(peptide): # zelimo da je konzistentan s ciklickim
  n = len(peptide) # duzina peptida
  mass = get_mass() # dohvati mase aminokiselina
  # postavi spektar na 0 // bez ukupne mase - razlika od prijasnjeg def
  spectrum = [0]
  for l in range(n): # za svaki n u dužini spektra
    for k in range(1, n - l + 1): # za svaki k od 1 do n-l+1
      # ne smijemo prijec preko peptida !!
      subpeptide = peptide[l : l + k] # napravi podpeptid
      spectrum.append(sum(subpeptide)) # u spektar dodaj sume subpeptida
  return sorted(spectrum) # vrati sortirani spektar


# je li linearni spektar konzistentan s ciklickim
def belongs_spectrum(candidate_spectrum, main_spectrum):
  # spektar kandidata iz linearning - racunamo broj pojavljivanja
  # rijecnik rijesenje
  counter_c_spectrum = Counter(candidate_spectrum)
  # spektar ciklicnog spektra
  counter_m_spectrum = Counter(main_spectrum)
  # za svaki kljuc vrijednost(broj pojavljivanja) iz kandidata
  for key, count in counter_c_spectrum.items():
    # ako nema kljuca (peptida) u ciklicnom spektru
    if key not in counter_m_spectrum:
      return False # vrati false
    # ako je broj pojavljivanja veci u linearnom od ciklicog za peptid
    if count > counter_m_spectrum[key]:
      return False # vrati false
  return True # inace vrati true

# ispituje masu i spektar kandidata
def check_cyclo(spectrum, peptide):
  parent_mass = max(spectrum) # masa spektra
  # ako je masa peptida jednaka sumi (masi spektra)
  # ako je ciklospektar peptida jednak spektru
  if sum(peptide) == parent_mass and cyclospectrum(peptide) == spectrum:
    return True #vrati istina
  return False # vrati laz


def check_linear(spectrum, peptide): #provjeri linearnost
  parent_mass = max(spectrum) # dohvati maksimum spektra
  # ako je zbroj svih peptida manji ili jednak masi maksimuma spektra
  # i ako linearni spektar peptida je konzistentan sa spektrom
  if sum(peptide) <= parent_mass and belongs_spectrum(
      linearspectrum(peptide), spectrum):
    return True #vrati true
  return False # vrati false

def branch_and_bound(spectrum):
  all_combinations = [] # niz svih kombinacija
  # dohvati sve mase aminokiselina - skup
  aa_masses = set(get_mass().values())
  # dohvati najvecu masu iz spektra(masa cijelog spektra)
  parent_mass = max(spectrum)
  peptides = [[]] #matrica peptida
  while True: # dok je istina
    # kandidati -> dodajemo pocetnim peptidima sve moguce mase
    # za svaki peptid iz liste peptida
    # na pocetku lista prazna pa sve se mase dodaju
    candidates = [peptide + [aa_mass] for aa_mass
                  in aa_masses for peptide in peptides]
    # provjeravamo zadovoljavaju konzistentnost, ako jesu dodajemo ih
    # inace izbacujemo
    selected = [peptide for peptide in candidates
                if check_linear(spectrum, peptide)]
    # u sve kombinacije dodajemo peptide iz spektra koji su konzistentnzi
    # provjeravamo masu i konzistentnost spektra kandidata
    all_combinations.extend([peptide for peptide in
                             selected if check_cyclo(spectrum, peptide)])
    # ubacujemo sve peptide iz izabranih kojima suma nije jednaka sumi peptida
    # koja nije jednaka -> ako je jednaka onda s njima nemamo sta radit
    peptides = [peptide for peptide in
                selected if sum(peptide) != parent_mass]
    if len(peptides) == 0: # kad je duljina peptida 0 - sve smo ih izbacili
      break # prekinut cemo petlju
    res = []
  for comb in all_combinations:
    res.append('-'.join(str(x) for x in comb))
  return ' '.join(sorted(res))


with open("rosalind_ba4e (3).txt", "r") as f:
  spectrum = f.readline().split()
spectrum = [int(x) for x in spectrum]
print(branch_and_bound(spectrum))