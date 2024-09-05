#include <iostream>
using namespace std;
 
// 函数声明
void swap(int *x, int *y);
 
int main ()
{
   // 局部变量声明
   int a = 100;
   int b = 200;
   int *c,*d;
   c=&a;
   d=&b;
   cout << "交换前，a 的值：" << *c << endl;
   cout << "交换前，b 的值：" << *d << endl;
 
   /* 调用函数来交换值 */
   swap(&a,&b);
   cout << "交换后，a 的值：" << *c << endl;
   cout << "交换后，b 的值：" << *d << endl;
 
   return 0;
}
 
// 函数定义，注意这里面改变参数的方法
void swap(int *x, int *y)
{
   int temp;
   cout << "调用的函数中的交换:"<<endl;
   cout  << *x <<endl;
   cout << *y <<endl;
   temp = *x; /* 保存地址 x 的值 */
   *x = *y;    /* 把 y 赋值给 x */
   *y = temp; /* 把 x 赋值给 y  */
   cout  << *x <<endl;
   cout << *y <<endl;
   return;
}