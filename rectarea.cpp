#include <iostream>

#include<bits/stdc++.h>

#include<cmath>

using namespace std;


int main()

{
    
int a=0,b=0,c=4,d=4,e=2,f=2,g=3,h=3;
    
int l1=c-a,b1=d-b,l2=g-e,b2=h-f,ar;
    
    
//cout<<l1<<b1<<l2<<b2;
    
if(l1>l2 && b1>b2)
    
ar=l2*b2;
    
    
else if(l1<l2 && b1<b2)
    
ar=l1*b1;
    
    
else if(l1>l2 && b1<b2)
   
ar=l2*(d-f);
    
    
else if(l1<l2 && b1>b2)
    
ar=l1*(c-e);
    
    
else if((g>c && h>d) && (e>a && f>b))
    
ar=(c-e)*(d-f);
    
    
cout<<ar;
    
return 0;

}
