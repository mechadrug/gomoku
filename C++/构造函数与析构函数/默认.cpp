class A{
    int x,y;
    char c;
    public:
        A(){
            x=y=0;
        };
        A(int i){
            x=i;y=0;
        };
        A(const char*p){
            c=*p;
        };

};

int main(){
    A a1;
    A a11=A();//两种调用默认构造函数的方法

    A a2=A(1);
    A a22=1;//A()可以直接省略

    A a[4];//创建四个对象,每个对象分别调用各自的吗,默认构造函数
    A b[5]={A(),A(1),A('aba'),2,'xyz'};//理解为数组的初始化
    
}