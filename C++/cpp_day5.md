# c++的λ

0. 整体表达：[capture list] (parameters) mutable throw()-> return-type{ statement}，可以直接使用，也可以作为函数入参出现，不能复用

1. 捕获列表[]:lambda引出符，标志着下文是lambda函数，同时可以捕捉上下文的变量供lambda函数使用

    - []不捕获任何变量，λ外的参数不可用
    - [var]值传递捕获变量var，创建一个副本
    - [=]值传递捕获所有父作用域的变量(包括this)
    - [&var]引用捕捉变量var
    - [&]引用捕捉所有父作用域的变量(包括this)
    - [this]值传递方式捕捉当前的this指针（？）
    - 混合使用：[&,a,b]a与b值传递，其他引用传递；[=,&a,&b]a与b引用传递，其他值传递
    - 报错：[=,a];[&,&this]重复捕捉。
2. 参数列表(type var1,type var2,...):如果不需要参数传递则**可以连同括号一起省略**

3. 可变规则 mutable：使用后，在lambda函数中创建一个捕获函数的副本进而可以改变该副本的值.mutable关键字必须要跟在参数列表后面，因此参数列表的括号必须保留(就算没有参数)

```c++
    int x = 10;
    auto lambda = [x]() mutable { 
        x = 20;  // 使用mutable后可以修改捕获的x
        std::cout << x << std::endl; 
    };
    lambda();  // 输出20
    std::cout << x << std::endl;  // 输出10，原来的x没有被改变
```

4. 异常说明throw():内部函数抛出异常

5. 使用auto可以省略->，不需要返回值也可以省略

6. `auto print = []{cout << "Hello World!" << endl; };`等价于：

```c++
    class print_class
    {
    public:
        void operator()(void) const
        {
            cout << "Hello World！" << endl;
        }
    };
    //用构造的类创建对象，print此时就是一个函数对象
    auto print = print_class();
```

- 上述类也可以叫做c++仿函数