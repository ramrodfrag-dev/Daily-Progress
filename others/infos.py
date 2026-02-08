

n=int(input())
A=[0] * n
for i in range(0,n):
    A[i]=int(input())

q=int(input())
queries=[]
result=0

for i in range(0,q):
    small=list(map(int,input().split()))
    queries.append(small)


for q in queries:
    if q[0]==1:
        l=q[1]
        r=q[2]
        for i in range(l,r+1):
            A[i]=(i-l+1)*A[l]
        
    elif q[0]==2:
        l=q[1]
        r=q[2]
        for i in range(l,r+1):
            result=result+A[i]
            
            
print(result)