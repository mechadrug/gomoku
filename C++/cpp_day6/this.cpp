#include<iostream>
using namespace std;

class Example {
private:
    int value;
public:
    void setValue(int value) {
        this->value = value; // 使用this来区分成员变量和参数
    }
};

class Example2 {
public:
    Example2& setA(int a) {//注意这里返回的不是拷贝，是引用，不然对于对象的数据成员无法改变
        // 做一些事情，可以是数据成员自增
        return *this; // 返回对象自身的引用
    }
};

class Example3 {
public:
    Example3* getThis() {
        return this; // 返回当前对象的指针
    }
};

class Base {
public:
    void display() { std::cout << "Base display\n"; }
};

class Derived : public Base {
public:
    void display() { std::cout << "Derived display\n"; }
    void show() {
        this->Base::display(); // 显式调用基类的display函数（通过当前对象调用base类的display方法）
    }
};

template <typename T>
class Base2 {
public:
    void helper() { 
        std::cout << "Base helper\n"; 
    }
};

template <typename T>
class Derived2 : public Base2<T> {
public:
    void func() {
        this->helper(); // 使用this来显式调用Base类的成员函数
    }
};
//在Derived类的func函数中，helper函数是从基类Base<T>继承的。
//如果我们直接调用helper()，编译器会报错，因为在模板类中，编译器无法确定helper是否来自基类（这是模板类的延迟绑定特性所致）。
//显式使用this->helper()告诉编译器，helper函数是通过当前对象来调用的，这使得编译器可以正确解析这个函数。

int main(){
    Derived2<int> d;
    d.func(); // 调用Base类的helper函数
    Example2 obj;
    obj.setA(5).setA(10); // 链式调用
}