#include <iostream>
using namespace std;
void push();
void pop();
int top=0,data,a[50],n=5;
int main()
{
    //cin>>n;
    push();
    pop();
    return 0;
}

void push()
{
    if (top==n)
    return;
    else
    {
    while(top<n)
{
    cin>>data;
top++;
a[top]=data;
}
}
}
void pop()
{
    if(top==0)
    return;
    else
    {
    while(top>0)
    {
        cout<<a[top];
    a[top]=0;
    top--;
}
}
}