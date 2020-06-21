#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
int m,n,k,i,j,f,t;
cin>>t;
while(t--)
{
cin>>n>>m;
vector <vector <int>> a (n,vector <int> (m)); 
for (i=1;i<=n;i++)
{
    for (j=1;j<=m;j++)
    cin>>a[i][j];
}
cin>>k; //element to be searched
    f=0;
    for (i=1;i<=n;i++)
    {
        if (a[i][1]<=k && k<=a[i][m])
        {f=i;
        break;}
    }
    if(f==0)
    cout<<0;
    else
    {
    for (i=1;i<=m;i++)
    {
    if(a[f][i]==k)
    cout<<1;
    break;
    }
    }
}    
    return 0;
}
