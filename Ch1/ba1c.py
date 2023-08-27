with open("rosalind_ba1c (2).txt","r") as f:
    string=f.readline().strip()

dict={'A':'T','T':'A','C':'G','G':'C'}

def replace_with_complement(text, compl):
    text2=''
    for s in text:
        if s in compl:
            text2 += compl[s]
            
    return text2[::-1]

print(replace_with_complement(string, dict))

