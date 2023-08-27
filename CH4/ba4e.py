import itertools

with open('rosalind_ba4e (2).txt','r') as f:
        numbers = list(map(int, f.readline().strip().split(' ')))
    
t = numbers.pop()  # Remove and store the last element as the threshold t
    

print(t)
def calculate_sum(permutation):
    return sum(permutation)


x=[]
for num in numbers:
  
    if int(num) <= 186 and int(num)>0:
        x.append(int(num))

with open('file_4e2.txt', 'w') as output_file:
    for perm in itertools.permutations(x):
        
        if calculate_sum(perm) <= t:
            output_file.write('-'.join(map(str, perm)) + '\n')
print(' dom')