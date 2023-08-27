import re

def ReverseComplement(text):
    text2=''
    dict={'A':'T','T':'A','C':'G','G':'C'}
    for s in text:
        if s in dict:
            text2 += dict[s]
            
    return text2[::-1]




def overlapping_matches(pattern, seq):
    return re.finditer(rf"(?=({pattern}))", seq)


def sharedKmers(k, s1, s2):
    for i in range(len(s1) - k + 1):
        seq = s1[i : (i + k)]
        for s in [seq, ReverseComplement(seq)]:
            match = list(overlapping_matches(s, s2))
            for m in match:
                yield (i, m.start())


with open("rosalind_ba6e.txt","r") as file:
    inlines= [line.strip() for line in file.readlines()]
    k=int(inlines[0])
    s1=inlines[1]
    s2=inlines[2]

res=sharedKmers(k,s1,s2)
for r in res:
    print(r)