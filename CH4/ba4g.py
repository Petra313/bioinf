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
     

def expand(peptides):
  # dohvati sve mase aminokiselina - skup
  aa_masses = set(get_mass().values())
  # novi peptidi -> dodajemo pocetnim peptidima sve
  # moguce mase za svaki peptid iz liste peptida
  # na pocetku lista prazna pa sve se mase dodaju
  new_peptides = [peptide + [aa_mass] for aa_mass
                  in aa_masses for peptide in peptides]
  return new_peptides # vrati nove peptidea
     

def Score(peptide, spectrum):
    pep_spec = cyclospectrum(peptide) # mase u ciklospektru
    result = 0 # postavi rezultat na 0
    # jedinstvene mase su skup (brojevi se ne ponavljaju)
    # teoretskog spektra i dobivenog spektra
    unique_masses = set(pep_spec + spectrum)
    for mass in unique_masses: # za svaku masu u jedinstvenim masama
      # u rezultat pribroji -> prebroji pojavljivanja u teoretskom spektru
      # ciklopeptida i dobivenom spektru te izmedu ta dva odaberi minimalni
      # broj pojavljivanja
      result += min(pep_spec.count(mass), spectrum.count(mass))
    return result # vrati rezultat
     

def Trim(leaderboard, spectrum, N):
  if len(leaderboard) <= N: # ako je duzina ljestvice manja ili  jednaka N
    return leaderboard # vrati ljestvicu
  scores = {} # rijecnik postignuca
  # za svaku poziciju i i masu peptida u ljestvici
  for i, peptide in enumerate(leaderboard):
    # postavi index kao kljuc, a vrijednost Score peptida u spektru
    scores[i] = Score(peptide, spectrum)
  # napravi sortianu listu vrijednosti iz scores silazno
  sorted_scores = sorted(scores.values(), reverse=True)
  # postavi kao prag N-1-vi element iz sortiranih postignuca
  threshold = sorted_scores[N - 1]
  # vrati mase peptida iz ljestvice koji imaju veci score od praga
  # pronadi index, score iz originalne ljestvice unutar scores i
  # usporedi s granciom
  return [leaderboard[idx] for idx, score
          in scores.items() if score >= threshold]
     

def leaderboard_cyclopeptide_sequencing(spectrum, N):
  leaderboard = [[]] # ljestvica je matrica
  leader_peptide = [] # vodeci peptid
  while leaderboard:
    leaderboard = expand(leaderboard) # prosiri ljestvicu
    for peptide in leaderboard: # za svaki peptid u ljestvici
      # zbroji mase peptida i ako su one jednake
      # zadnjoj masi spektra(ukupna masa spektra)
      if sum(peptide) == spectrum[-1]:
        # ako je score peptida napram spektru vece od score-a vodeceg peptida
        # napram spektru
        if Score(peptide, spectrum) > Score(leader_peptide, spectrum):
          # postavi da je vodeci peptid onaj peptid koji ima veci score
          leader_peptide = peptide
      # inace ako je suma masa veca od ukupne sume spektra
      elif sum(peptide) > spectrum[-1]:
        # ljestvica je jednaka svim peptidima u ljestvici koji su
        # razliciti od trenutnog peptida koji ima vecu masu
        leaderboard = [pep for pep in leaderboard if pep != peptide]
    # vrati N peptida
    leaderboard = Trim(leaderboard, spectrum, N)
  return '-'.join(str(x) for x in leader_peptide) # vrati vodeci peptid

ans = leaderboard_cyclopeptide_sequencing([0, 71, 113, 129, 147,
                                     200, 218, 260, 313, 331,
                                     347, 389, 460], 10)


with open("rosalind_ba4g.txt", "r") as f:
  N = int(f.readline().strip())
  spect = f.readline().split()
spectrum_ = [int(x) for x in spect]
res = leaderboard_cyclopeptide_sequencing(spectrum_, N)
print(res)

     