#include<iostream>
using namespace std;

struct Demo 
{
  char name[10000];
  int  count;
};

int main()
{
  Demo my_demo = {0};
  Demo *my_demo_p = &my_demo;
  Demo &my_demo_ref = my_demo;
  
  // 方式1：传递实参  
  func1(my_demo);

  // 方式2：传递指针  
  func2(my_demo_p);

  // 方式3：传递引用  
  func3(my_demo_ref);

  return 0;
}
//如上所示，参数传递可以有三种方式，则三种函数可以这样定义：

// 方式1：传递实参 
void func1(Demo demo)
{
  cout << demo.name;
}

// 方式2：传递指针  
void func2(const Demo *demo_p)
{
  cout << demo_p->name;
}

// 方式3：传递引用  
void func3(const Demo &demo_ref)
{
  cout << demo_ref.name;
}