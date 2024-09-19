#include <iostream>

class Member1 {
public:
    Member1() { std::cout << "Member1 constructor" << std::endl; }
    ~Member1() { std::cout << "Member1 destructor" << std::endl; }
};

class Member2 {
public:
    Member2() { std::cout << "Member2 constructor" << std::endl; }
    ~Member2() { std::cout << "Member2 destructor" << std::endl; }
};

class Base {
public:
    Base() { std::cout << "Base constructor" << std::endl; }
    ~Base() { std::cout << "Base destructor" << std::endl; }
};

class Derived : public Base {
    Member1 m1;
    Member2 m2;
public:
    Derived() { std::cout << "Derived constructor" << std::endl; }
    ~Derived() { std::cout << "Derived destructor" << std::endl; }
};
class A {
    int y=2;
    int x=7;//这里先声明了y,最后出来的值一律视为1(不管x是否在下面的初始化成员列表出现了,都会导致y初始化时直接先绑定到x+1,此时还没有到x的初始化)
public:
    A() : y(x+1),x(10) {//这里的初始化会覆盖上面的初始化;调换这里的顺序并没有用
        std::cout << "x = " << x << ", y = " << y << std::endl;
    }
};
int main() {
    Derived d;
    A a;//如果有相互依赖关系的成员对象(y依赖于x),需要保证先声明x.
    return 0;
    
}
