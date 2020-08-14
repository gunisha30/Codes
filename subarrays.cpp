//iterative
#include <iostream>

using namespace std;

int main()
{
    vector <int> a={1,2,3};
    int i=0,j=0,k=0,n=a.size();
    for (i=0;i<n;i++)
    {
        for (j=i;j<n;j++)
        {
            for(k=i;k<=j;k++)
            cout<<a[k]<<" ";
        }
    }
    

    return 0;
}

//recursive
#include <bits/stdc++.h>
using namespace std;

void solve(vector <int> ar, int st, int en)
{
    if(en==ar.size())
    return;
    
    else if(st>en)
    solve(ar,0,en+1);
    
    else
    {
        cout<<"[ ";
        for (int i=st;i<en;i++)
        cout<<ar[i]<<" ";
    
        cout<<ar[en]<<" ]"<<endl;
        solve(ar,st+1,en);
    }
}

int main()
{
    vector <int> ar={1,2,3,4};
    solve(ar,0,0);

    return 0;
}
