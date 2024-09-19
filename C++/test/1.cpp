#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
    int arr[] = {1, 2, 3, 4, 5};
    vector<int> vec(arr, arr + 5);  // 使用数组初始化 vector
    for(auto v:vec){
        cout<<v<<" ";
        
    }
    return 0;
}