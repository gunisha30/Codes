 #link to the problem : https://practice.geeksforgeeks.org/problems/bleak-numbers/0 
 def bin(p):
    if (p>1):
        bin(p//2)
    a.append(p%2)
    return(a.count(1))
def f(n):
    for k in range(1,n):
        d=bin(k)
        if (k + d==n):
            return 1
    return 0
t=int(input())
while(t):
    n=int(input())
    a=[]
    i=f(n)
    print(i)
    t=t-1  
