#include<iostream>
#include<cstring>
using namespace std;
class String {
    int len;
    char *str;
public:
    String(const char* s) {
        len = strlen(s);  // 计算传入的字符串长度
        str = new char[len + 1];  // 动态分配内存来存储字符串，包括末尾的 '\0'
        strcpy(str, s);  // 将传入的字符串复制到新分配的内存中
    }
~String() {
    delete[] str;  // 释放动态分配的内存
    len = 0;
    str = NULL;//不是必须的,但可以避免悬空指针的问题
}
};
void f() {
    String s1("abcd");  // 创建对象 s1，调用构造函数
    // 其他操作...
}  // 函数结束时，调用析构函数
