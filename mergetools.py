problem link: https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=false
def merge_the_tools(s, k):
    def f(b):
        for i in range(0,len(b)):
            a=[]
            for j in b[i]:
                if j not in a:
                    a.append(j)
            print("".join(a))
    n=int(len(s)/k)
    p=0
    b=[]
    for i in range(0,n):
        a=[]
        for j in range(0,k):
            a.append(s[p])
            p=p+1
        s1="".join(a)
        b.append(s1)
    f(b)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
