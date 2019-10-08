import numpy as np
t=int(input())
while(t):
    r,c,q=map(int,input().split())
    a = np.zeros((r, c), dtype=int)
    while(q):
        i,j=map(int,(input().split()))
# a=list(map(int,input(split()))
# mat=np.array(a).reshape(r,c)
        def add(a,i,j):
            for p in range(r):
                a[p][j]=a[p][j]+1
            for q in range(c):
                a[i][q]=a[i][q]+1
            return a
        b=add(a,i,j)
        q=q-1
        #print(b)
#odd=list(filter(lambda x:(x%2!=0),a))
    c=0
    for j in range(r):
        odd=[i for i in b[j] if (i%2!=0) ]
        c=c+len(odd)
    print(c)
    t=t-1