Question: It can be seen that the number 125874, and its double, 251748, contain exactly the same digits, but in a
different order. Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
i=1
def f(l1,l2,l3,l4,l5):
    l1.sort()
    l2.sort()
    l3.sort()
    l4.sort()
    l5.sort()
    return(l1,l2,l3,l4,l5)
while(True):
    a=2*i
    b=3*i
    c=4*i
    d=5*i
    e=6*i
    l1 = list(map(int,str(a)))
    l2 = list(map(int,str(b)))
    l3 = list(map(int,str(c)))
    l4 = list(map(int,str(d)))
    l5 = list(map(int,str(e)))
    p,q,r,s,t=f(l1,l2,l3,l4,l5)
    if(p==q==r==s==t):
        print(i)
        break
    i=i+1
