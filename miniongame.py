link to the problem: https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(s):
    l=[]
    l1=[]
    l2=[]
    c1=0
    c2=0
    l = [s[i: j] for i in range(len(s)) 
          for j in range(i + 1, len(s) + 1)]
    for i in range(0,len(l)):
        if (l[i] not in l1) and (l[i][0] in ('A','E','I','O','U')):
            l1.append(l[i])
        if (l[i] not in l2) and (l[i][0] not in ('A','E','I','O','U')):
            l2.append(l[i])
    for i in l1:
        n=co(s,i)
        c1=c1+n
    for i in l2:
        n=co(s,i)
        c2=c2+n
    if(c1>c2):
        print("Kevin {}".format(c1))
    if(c1>c2):
        print("Kevin {}".format(c1))
    elif(c2>c1): 
        print("Stuart {}".format(c2))
    else:
        print("Draw")

def co(string, sub_string):
    c=0
    for i in range(0,len(string)):
        if(string[i:i+len(sub_string)]==sub_string):
            c=c+1
    return c
if __name__ == '__main__':
    s = input()
    minion_game(s)
