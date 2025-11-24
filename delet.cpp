#include<iostream>
using namespace std;
class node{
    public:
    int data;
    node*next;
    node(int value){
        data=value;
        next=NULL;
    }
};
node*linkedlist(int arr[],int index,int size){
    if(index==size)
    return NULL;
    node*temp;
    temp=new node(arr[index]);
    temp->next=linkedlist(arr,index+1,size);
    return temp;
}
int main(){
    node*head=NULL;
    int arr[5]={1,2,3,4,5};
    head=linkedlist(arr,0,5);
    if(head!=NULL){
        node*temp=head;
        head=head->next;
        delete temp;

    }
      node* tem = head;
    while(tem != NULL){
        cout << tem->data << " ";
        tem = tem->next;
    }


return 0;
}