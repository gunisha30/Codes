def f(s):
    dis=[]
    f=0
    for i in range(0,len(s)):
        if(s[i] not in dis):
            dis.append(s[i])
            c=s.count(s[i])
            if(c==1):
                return ('NO')
            else:
                for i in range(2,c):
                    if ((c % i) == 0):
                        return('NO')
    no=len(dis)
    if(no==1):
        return ('NO')
    else:
        for i in range(2,no):
            if ((no % i) == 0):
                f=1
                return ('NO')
        if(f==0):
            return ('YES')
        

    
t=int(input())
while(t):
    s=input()
    s1=f(s)
    print(s1)
    t=t-1