import random

def get_kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i : (i + k)]


def get_kmers(text, k):
    """Find indices of all k-mers in text"""
    kmers = set()
    for i in range(0, len(text) - k + 1):
        kmers.add(get_kmer(text, i, k))
    return kmers

def pattern_prob(pattern, profile):
    """return the probability of observing the pattern with the profile matrix"""
    prob = 1
    for index, letter in enumerate(pattern):
        prob *= profile[letter][index]
    return prob


def profile_most_probable(text, k, profile):
    """
    Find a Profile-most probable k-mer in a string text.
    Profile matrix is represented as a dict.
    """
    max_kmer = ""
    max_p = -1
    kmers = get_kmers(text, k)
    for kmer in kmers:
        tmp = pattern_prob(kmer, profile)
        if tmp > max_p:
            max_kmer = kmer
            max_p = tmp
    return max_kmer


def get_motifs(dna_list, profile):
    k = len(profile["A"])

    motifs = [profile_most_probable(dna_string, k, profile) 
              for dna_string in dna_list]
    return motifs


def create_profile_matrix(pattern_list, pseudo_counts=False):
    """
    Returs a profile matrix as a dict based on a the list patternlist
    """

    k = len(pattern_list[0])

    profile_matrix = {}
    profile_matrix["A"] = [0] * k
    profile_matrix["C"] = [0] * k
    profile_matrix["G"] = [0] * k
    profile_matrix["T"] = [0] * k

    for pattern in pattern_list:
        for index, letter in enumerate(pattern):
            profile_matrix[letter][index] = profile_matrix[letter][index] + 1

    if pseudo_counts:
        profile_matrix["A"] = [x + 1 for x in profile_matrix["A"]]
        profile_matrix["C"] = [x + 1 for x in profile_matrix["C"]]
        profile_matrix["G"] = [x + 1 for x in profile_matrix["G"]]
        profile_matrix["T"] = [x + 1 for x in profile_matrix["T"]]

    for i in range(0, k):
        total = (
            profile_matrix["A"][i]
            + profile_matrix["C"][i]
            + profile_matrix["G"][i]
            + profile_matrix["T"][i]
        )
        profile_matrix["A"][i] = profile_matrix["A"][i] / total
        profile_matrix["C"][i] = profile_matrix["C"][i] / total
        profile_matrix["G"][i] = profile_matrix["G"][i] / total
        profile_matrix["T"][i] = profile_matrix["T"][i] / total
    return profile_matrix


def score(motifs):
    """
    Score discrepancy in motifs
    """
    zzip = zip(*motifs)

    max_count = []
    for x in zzip:
        n_a = sum([y == "A" for y in x])
        n_c = sum([y == "C" for y in x])
        n_g = sum([y == "G" for y in x])
        n_t = sum([y == "T" for y in x])
        max_count.append(len(motifs) - max(n_a, n_c, n_g, n_t))

    return sum(max_count)


def randomized_motif_search_atom(dna_list, k):

    n_dna = len(dna_list[0])

    randpos = [random.randint(0, n_dna - k) for dna in dna_list]
    bestmotifs = [dna[index : (index + k)] for index, dna in zip(randpos, dna_list)]
    motifs = bestmotifs

    while True:
        profile = create_profile_matrix(motifs, pseudo_counts=True)
        motifs = get_motifs(dna_list, profile)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
        else:
            return bestmotifs


def randomized_motif_search(dna_list, k, n_runs=1000):
    """
    Returns best motifs
    """
    bestmotifs = randomized_motif_search_atom(dna_list, k)
    for _ in range(n_runs):
        motifs = randomized_motif_search_atom(dna_list, k)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs

with open("rosalind_ba2f.txt") as f:
    k, t = map(int, f.readline().strip().split())
    dna = [line.strip() for line in f]

result=randomized_motif_search(dna,k,2000)

for res in result:
    print(res)