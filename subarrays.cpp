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
