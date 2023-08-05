#include<iostream>
using namespace std;

void linearsearch(int arr[],int n)
{
    int temp=-1;

    for(int i=0; i<5; i++)
    {
        if(arr[i]==n){
            cout<<"match found"<<endl;
        temp=0;
        break;
    }}
    if (temp == -1)
    {
        cout << "No Element Found" << endl;
    }





}
int main()
{
    int n;
    int arr[5]= {2,1,7,3,10};
    cout<<"1 element to search"<<endl;
    cin>>n;

    linearsearch(arr,n);

}
