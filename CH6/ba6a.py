from copy import deepcopy

with open("rosalind_ba6a (3).txt", "r") as f:
    line = f.readline().strip()

# Remove the parentheses and split the line by spaces
values_with_signs = line[1:-1].split()

# Initialize an empty list to store the actual signed integers
signed_integers = []

for value in values_with_signs:
    sign = value[0]
    number = int(value[1:])
    
    if sign == "+":
        signed_integers.append(number)
    elif sign == "-":
        signed_integers.append(-number)


sorted_ind=0
per=[]
lon=len(signed_integers)
error_cnt = 0
for i in range(1,lon+1):
    a=[i,i*(-1)]
    intersection = set(a) & set(signed_integers)
    inter=list(intersection)
    try:
        index = signed_integers.index(inter[0])
    except IndexError as e:
        error_cnt += 1
        # print(f'a {a}')
        # print(f'inter[0] {inter}')
        # print(f'signed_integers {signed_integers}')
        # print(310 in signed_integers)
        # print(-310 in signed_integers)
    if index==sorted_ind and inter[0]!=i*(-1):
        sorted_ind=sorted_ind+1
        continue
    sliced_list = signed_integers[sorted_ind:index+1]
    reversed_list = [-num for num in sliced_list[::-1]]
    prex=signed_integers[0:sorted_ind]
    suf=signed_integers[index+1:lon]
    sorted_ind=sorted_ind+1
    signed_integers=prex+reversed_list+suf
    # print(signed_integers)

    per.append(signed_integers)
    # print(per)

    if signed_integers[sorted_ind-1]<0:
        signed_integers = deepcopy(signed_integers)
        signed_integers[sorted_ind-1]=signed_integers[sorted_ind-1]*(-1)
        per.append(signed_integers)
        # print(sig_int)
        # print(per)

        # signed_integers[sorted_ind-1]=signed_integers[sorted_ind-1]*(-1)
        # per.append(signed_integers)
        # print(signed_integers)
        # print(per)

# print(per)

with open('result_ba6a-j.txt', 'a') as file:
    for p in range(0,len(per)):
        res = '(' + ' '.join([('+' if pr > 0 else '') + str(pr) for pr in per[p]]) + ')'
        print(res)
        file.write(res + '\n' if len(per) != p else '')
print(error_cnt)

# for p in range(0,len(per)):
#     res = '(' + ' '.join([('+' if pr > 0 else '') + str(pr) for pr in per[p]]) + ')'
    # print('(' + ' '.join([('+' if pr > 0 else '') + str(pr) for pr in per[p]]) + ')')

    # print('(',end='')
    # for pr in per[p]:
       
    #      if pr>0:
    #          print('+', end='')
    #      print(pr, end=' ')
    # print(')',end='\n')