Link to the problem: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0
t=int(input())
while(t):
    a=[]
    b=[]
    size=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    def swap(l,i,j):
        t=l[i]
        l[i]=l[j]
        l[j]=t
    for i in range(0,len(b)):
        for j in range(i+1,len(b)):
            if(b[i]>b[j]):
                swap(b,i,j)
                swap(a,i,j)
                swap(c,i,j)
    print(c[0],end=" ")
    i=0
    for j in range(1,len(b)-1):
        if(a[j]>=b[i]):
            i=j
            print(c[j],end=" ")
    print("")
    t=t-1
    
