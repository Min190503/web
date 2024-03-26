#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a, s=0; 
    cout<<"Nhap so tien gui: ";
    cin>>a;
    for(int i = 0; i<=9 ; i++){
        a = a + a*0.051;
    }
        cout<<a;
    for(int j = 0;j < 10000; j++)
    {
        a = a + a*0.051;
        s = s+1;
        if(a = 50000000)
        cout<<s;
        break;
    }
}