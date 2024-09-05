//这是myclass.h
class MyClass
{
public:
 void setA(int _a);//普通的成员函数，函数声明和定义分别定义在函数的内部和外部，不要求在同一个文件
 //适合大型函数，缩减单个文件代码量，提高可读性
 void setB(int _b)   //隐式的内联函数，函数的声明和定义都定义在函数的内部
   {
     b = _b;
    }
    //较小的，能够被频繁调用的函数一般会作为隐式内联函数，避免开销，提高性能
 inline void setC(int _c); //显式的内联函数，使用关键字inline
                            //函数声明在类的内部，函数定义在类的外部，但是函数声明和定义必须在同 
                            //一个文件
private:
    int a;
    int b;
    int c;
};
 
inline void MyClass::setC(int _c)    //显式的内联函数，函数定义跟函数声明必须再同一个文件
{
  c = _c;
}
//必须要在同一个文件内！！可以使得类的代码块更加简洁