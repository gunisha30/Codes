link to the problem: https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(s):
    l=[]
    l1=[]
    l2=[]
    s1=""
    c1=0
    c2=0
    for i in range(0,len(s)):
        l.append(s[i])
    for i in range (0,len(s)):
        s1=l[i]
        for j in range(i+1,len(s)):
            s1=s1+l[j]
            if s1 not in l:
                l.append(s1)
    #print(l)
    for i in range(0,len(l)):
        if (l[i] not in l1) and (l[i][0] in ('A','E','I','O','U')):
            l1.append(l[i])
        if (l[i] not in l2) and (l[i][0] not in ('A','E','I','O','U')):
            l2.append(l[i])
    #print(l1)
    #print(l2)
    for i in l1:
        n=co(s,i)
        c1=c1+n
    for i in l2:
        n=co(s,i)
        c2=c2+n
    if(c1>c2):
        print("Kevin {}".format(c1))
    else: 
        print("Stuart {}".format(c2))

def co(strng,pat):
    res = [i for i in range(len(strng)) if strng.startswith(pat, i)] 
    return len(res)
if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
