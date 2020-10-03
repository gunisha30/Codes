#include <iostream>
#include <bits/stdc++.h>
#include <cmath>
using namespace std;

int main()
{
    int n,c=0,j,i;
    cin>>n;
    vector <int> prime (n+1,1);
    prime[0]=0;
    prime[1]=0;
    for(i=2;i<=n;i++)
    {
    if(prime[i]==1)
    {
        for(j=2;(i*j)<=n;j++)
    {
        prime[i*j]=0;
    }
    }
    }
    for (i=0;i<=n;i++)
    {
        if(prime[i])
        c++;
    }
    cout<<c;
    return 0;
}
