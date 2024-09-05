#include "test.h"
#include<iostream>
using namespace std;

void test::myFunction(int x, int y=3) {
    int t=x+y;
    cout<<t;
}//不可以再次定义，因为在test1中已经定义过了

// 调用 myFunction
int main() {
    test obj;  // 正确声明对象
    obj.myFunction(5);  // 使用默认参数y = 10
    return 0;
}