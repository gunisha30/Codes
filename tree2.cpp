#include<iostream.h>

#include<conio.h>

#define NULL 0

class tree
    
{
     
public:
            
int value, *left, *right;  
                       
void insert(int);
    
};
tree* tree::insert(int idata)
            
{
            
tree* obj;
            
obj->value=idata;
            
obj->left=NULL;
            
obj->right=NULL;
            
return obj;
            
}
    

void main()

{
    
clrscr();
tree* node=insert(9);
    
node->left=insert(10);
    
node->right=insert(11);
    
cout<<root->value;
getch();
}