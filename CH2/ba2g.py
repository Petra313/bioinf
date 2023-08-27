from random import randint, choices


def RandomSelectMotifs(Dna, k, t):
  Motifs = []
  for seq in Dna:
    index = randint(0, len(seq) - k)
    Motifs.append(seq[index:index+k])

  return Motifs

def Profile(Motifs, k):
  profile = []
  for i in range(k):
    for j in range(len(Motifs)):
      if j == 0:
        profile.append({ 'A': 1, 'T': 1, 'C': 1, 'G': 1 })
      profile[i][Motifs[j][i]] += 1
  return profile

def Motif(profile, Seq, k):
  probs = []
  for i in range(len(Seq) - k + 1):
    Sum = 1
    for j in range(k):
      Sum *= (profile[j][Seq[i+j]])
    probs.append(Sum)

  return probs

def Score(Motifs, k, t):
  profile = Profile(Motifs, k)
  score = 0
  for a in range(len(profile)):
    score += (4 + t - profile[a][max(profile[a], key=profile[a].get)])
  return score

def GibbsSampler(Dna, k, t, N):
  Motifs = RandomSelectMotifs(Dna, k, t)
  BestMotifs = list(Motifs)
  for j in range(N):
    i = randint(0, t - 1)
    Motifs.pop(i)
    profile = Profile(Motifs, k)

    temp = Motif(profile, Dna[i], k)
    index = choices(list(range(0, len(Dna[i]) - k + 1)), temp)

    Motifs.insert(i, Dna[i][index[0]:index[0] + k])

    if Score(Motifs, k, t) < Score(BestMotifs, k, t):
      BestMotifs = list(Motifs)
  return BestMotifs

with open('rosalind_ba2g.txt', 'r') as f:
  k, t, N = [int(x) for x in f.readline().strip().split(' ')]
  Dna = [x.strip() for x in f.readlines()]

  BestMotifs = GibbsSampler(Dna, k, t, N)

  for i in range(0, 20):
    Motifs = GibbsSampler(Dna, k, t, N)
    if Score(Motifs, k, t) < Score(BestMotifs, k, t):
      BestMotifs = Motifs

resut=BestMotifs
for res in resut:
  print(res)