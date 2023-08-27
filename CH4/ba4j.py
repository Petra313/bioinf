def generate_substrings(input_str: str, gram: int=2):
    len_input = len(input_str)
    if len(input_str) == gram:
        return [input_str]
    if len(input_str) == 1:
        return [i for i in input_str]
    substrings = []
    for i in range(len_input-gram+1):
        substring = input_str[i:i+gram]
        substrings.append(substring[:gram])
        print(substring[:gram])
    return substrings

mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }



with open('rosalind_ba4j.txt','r') as f:
    string=f.readline().strip()
s=string
new_dict = {}
new_tuple = []
for i in range(1,len(s)+1):
    outputs = generate_substrings(s, i)
    for term in outputs:
        res = 0
        for letter in term:
            res += mass[letter]
        new_dict.update({term: res})
        new_tuple.append((term, res))

new_dict = {k: v for k, v in sorted(new_dict.items(),key=lambda item:item[1])}
new_tuple = [item[1] for item in sorted(new_tuple,key=lambda item:item[1])]

print(' '.join(['0'] + [str(v) for v in new_tuple]))
