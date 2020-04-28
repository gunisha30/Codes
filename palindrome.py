s='madam'
s1=s[::-1]
mid=len(s)//2
if(len(s)%2==0):
    if(s[0:mid]==s1[0:mid]):
        print('yes')
    else:
        print('no')
else:
    if(s[0:mid+1]==s1[0:mid+1]):
        print('yes')
    else:
        print('no') 
       
#code to print all substrings of a string 
s=input()
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        l.append(s[i:j])
print(l)
    
