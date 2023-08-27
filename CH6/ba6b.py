from copy import deepcopy

with open("rosalind_ba6b.txt", "r") as f:
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

breakpoints=0
prev=0
next=signed_integers[0]
for i in range(0,len(signed_integers)):
    if abs(abs(prev)-abs(next))!=1:
        breakpoints=breakpoints+1
    else:
        if abs(prev)-abs(next)==1 and prev>0:
            breakpoints=breakpoints+1
        elif abs(prev)-abs(next)==-1 and prev<0:
            breakpoints=breakpoints+1
    if i+1== len(signed_integers):
        next=len(signed_integers)+1
    else:
        prev=next
        next=signed_integers[i+1]
print(breakpoints)


            
    