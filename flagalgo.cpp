#include <iostream>


using namespace std;


int main()

{
    
int k,n;
	
cin>>k>>n;
	
int a[n];
	
for(int i=0;i<n;i++)
	
cin>>a[i];
	
int l=0,h=n-1,m=0;
	
while(m<=h)
	
{
	    
switch(a[m])
	    
{
	        
case 0:
	        
swap(a[l],a[m]);
	        
l++;m++;
	        
break;
	    
	        
case 1:
	        
m++;
	        
break;
	    
	        
case 2:
	        
swap(a[m],a[h]);
	        
h--;
	        
break;
	    
}
	
}

for(int i=0;i<n;i++)
	
cout<<a[i];
	
return 0;

}

void swap(int n,int m)
    
{
	    
int t;
	    
t=m;
	    
m=n;
	    
n=t;
	
}