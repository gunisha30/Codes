t=int(input())

def f(s):
    l=[]
    rev=[]
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            a=s[i:j]
            l.append(a)
    for i in l:
        m="".join(reversed(i))
        if(m==i):
            rev.append(i)
    k=max(rev, key=len)
    print(k)
while(t):
    s=input()
    f(s)
    t=t-1

