#include <iostream>

using namespace std;

void insertionsort(int arr[]) {
  int key=0;
  int j=0;
  for(int i=0;i<5;i++)
  {
     key=arr[i];
     int j=0;
     while(j>=0&& arr[j]>key)
     {
         arr[j+1]=arr[j];
         j=j-1;
     }
  }arr[j+1]=key;

}


int main()
{

    int arr[5];

    cout<<"5 digits"<<endl;
    for(int i=0; i<5; i++)
    {
        cin>>arr[i];
    }
    cout<<"Before sorting:"<<endl;
    for(int i=0; i<5; i++)
    {
        cout<<arr[i]<<" ";
    }


    insertionsort(arr);

    cout << endl << "After Sorting: " << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << " ";
    }
}
