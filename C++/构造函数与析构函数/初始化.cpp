class init{
    int x=1;
    const int value=42;//c++11之后是允许的
    int &ref=x;//引用成员通过非静态数据成员初始化器初始化也是允许的
    public:
    init(int v):value(v){};//构造函数中的初始化列表覆盖默认值
};