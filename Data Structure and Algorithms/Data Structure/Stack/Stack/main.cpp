#include <iostream>
#include <string>
using namespace std;

class Stack
{

private:
    int top;
    int arr[5];

public:
    Stack()
    {
        top=-1;
        for(int i=0; i<5; i++)
        {
            arr[i];
        }


    }

    bool isempty()
    {
        if (top==-1)
            return true;
        else
            return   false;

    }
    bool isfull()
    {
        if (top==4)
        {
            return true;
        }
        else
            return false;

    }

    void push(int val)
    {
        if (isfull())
            cout<<"stack overflow"<<endl;
        else
        {
            top++;
            arr[top]=val;
        }
    }
    int pop()
    {
        if(isempty())
        {
            cout<<"Stack underflow"<<endl;
            return 0;
        }
        else
        {

            int popvalue=arr[top];
            arr[top]=0;
            top--;
            return popvalue;

        }
    }
    int count()
    {
        return (top+1);

    }
    int peek(int pos)
    {

        if(isempty())
        {
            cout<<"UNDerflow";
        }
        else
        {
            return arr[pos];
        }
    }

void change(int pos,int val){
arr[pos]=val;
cout<<"change value location "<<pos<<endl;



}
void display(){

cout<<"All values"<<endl;

for (int i=4;i>=0;i--){
    cout<<arr[i]<<endl;
}


}



};








int main()
{



}
