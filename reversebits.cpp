//reverse digits
#include <iostream>

using namespace std;

int main()
{
int i=0;
unsigned long int a, num=0;
cin>>a;
while(a)
{
    //shifting is faster than pow function 
    num=num+((a%2)*1<<(3-i));
    a=a/2;
    i++;
}
cout<<num;
//cout<<((1<<3)+10); 
return 0;
}
