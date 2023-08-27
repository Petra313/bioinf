with open('rosalind_ba4b (1).txt','r') as f:
    string=f.readline().strip()
    amino=f.readline().strip()


def replace_with_complement(text, compl):
    text2=''
    for s in text:
            text2 += compl[s]
            
    return text2[::-1]
def DNAtoRNA(text):
     text2=''
     for s in text:
            if s=='T':
                 text2=text2+'U'
            else:
                 text2=text2+s
     return text2
        
    
dict={'A':'T','T':'A','C':'G','G':'C'}

codon_table = {
        "AAA": "K",
        "AAC": "N",
        "AAG": "K",
        "AAU": "N",
        "ACA": "T",
        "ACC": "T",
        "ACG": "T",
        "ACU": "T",
        "AGA": "R",
        "AGC": "S",
        "AGG": "R",
        "AGU": "S",
        "AUA": "I",
        "AUC": "I",
        "AUG": "M",
        "AUU": "I",
        "CAA": "Q",
        "CAC": "H",
        "CAG": "Q",
        "CAU": "H",
        "CCA": "P",
        "CCC": "P",
        "CCG": "P",
        "CCU": "P",
        "CGA": "R",
        "CGC": "R",
        "CGG": "R",
        "CGU": "R",
        "CUA": "L",
        "CUC": "L",
        "CUG": "L",
        "CUU": "L",
        "GAA": "E",
        "GAC": "D",
        "GAG": "E",
        "GAU": "D",
        "GCA": "A",
        "GCC": "A",
        "GCG": "A",
        "GCU": "A",
        "GGA": "G",
        "GGC": "G",
        "GGG": "G",
        "GGU": "G",
        "GUA": "V",
        "GUC": "V",
        "GUG": "V",
        "GUU": "V",
        "UAA": "*",
        "UAC": "Y",
        "UAG": "*",
        "UAU": "Y",
        "UCA": "S",
        "UCC": "S",
        "UCG": "S",
        "UCU": "S",
        "UGA": "*",
        "UGC": "C",
        "UGG": "W",
        "UGU": "C",
        "UUA": "L",
        "UUC": "F",
        "UUG": "L",
        "UUU": "F",
}
num=len(amino)
def prijevod(string,codon_table):
    final=''
    for i in range(0,len(string)-2,3):
        subs=string[i:i+3]
        final=final+codon_table[subs]
    return final

dna_all=[]
dna_all.append(string)
dna_all.append(string[1:])
dna_all.append(string[2:])

pr=prijevod(DNAtoRNA(string),codon_table)
pr2=prijevod(DNAtoRNA(string[1:]),codon_table)
pr3=prijevod(DNAtoRNA(string[2:]),codon_table)


string_2=replace_with_complement(string,dict)
dna_all.append(string_2)
dna_all.append(string_2[1:])
dna_all.append(string_2[2:])
pr_2=prijevod(DNAtoRNA(string_2),codon_table)
pr_3=prijevod(DNAtoRNA(string_2[1:]),codon_table)
pr_4=prijevod(DNAtoRNA(string_2[2:]),codon_table)

all=[]
all.append(pr)
all.append(pr2)
all.append(pr3)
all.append(pr_2)
all.append(pr_3)
all.append(pr_4)

for i in range(3):
    for j in range(0,len(all[i])-len(amino)+1):
        subs=all[i][j:j+len(amino)]
        if subs==amino:
             print(dna_all[i][j*3:j*3+3*len(amino)])

for i in range(3,6):
    for j in range(0,len(all[i])-len(amino)+1):
        subs=all[i][j:j+len(amino)]
        if subs==amino:
             print(replace_with_complement(dna_all[i][j*3:j*3+3*len(amino)],dict))
