import SHA256
import random

def check_prime(n):
    flag=0
    n1=int((n/2)-0.5)
    for i in range(2,n1):
        if n%i==0:
            flag=1
            break
        else:
            flag=0

    return(flag)


p=random.randint(50,100)
while(check_prime(p)!=0):
    p=random.randint(50,100)
p1=int(p-1)
q=2

for i in range(int(p1/2),2,-1):
    if p1%i==0:
        if check_prime(i)==0:
            q=i
            break

h=random.randint(1,p1)
p1q=p1/q
g=(pow(h,p1q))%p

x=random.randint(1,q)
y=(pow(g,x))%p
k=random.randint(1,q)

r1=(pow(g,k))%p
r=r1%q

hash_val=SHA256.hash_value

s1=int(hash_val,16)+(x*r)
s2=s1/k
s=s2%q
print('p ',p,'\nq ',q,'\ng ',g,'\nx',x,'\ny',y,'\nk',k,'\nr',r,'\ns',s)
