with open('rosalind_ba1m (3).txt','r') as f:
    num=int(f.readline().strip())
    num2=int(f.readline().strip())

def text_to_num(k,n):
   pat=''
   for i in range(n):
        i=k%4
        if i==0:
         c='A'
        elif i==1:
            c='C'
        elif i==2:
            c='G'
        else:
            c='T'
        k=k//4
        pat=c+pat
   return pat


print(text_to_num(num,num2))
