#include<iostream>
using namespace std;
int print(int value,int base=10){
    int k=value+base;
    return k;
}
int main(){
    int a=print(19,2);
    int b=print(13);
    cout<<a<<b;
    return 0;
}