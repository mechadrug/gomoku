#include "test.h"
#include<iostream>
using namespace std;

void test::myFunction(int x, int y) {
    int t=x+y;
    cout<<t;
}
// 调用 myFunction
int main() {
    test obj;  // 正确声明对象
    obj.myFunction(5);  // 使用默认参数y = 10
    return 0;
}