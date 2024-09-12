#include<iostream>
using namespace std;

class Date
{
    public:
        void set(int y,int m,int d){//成员函数
            year=y;month=m;day=d;
        }
        bool IS_LEAP_YEAR()//成员函数
        {
            return (year%4==0&&year%100!=0)||(year%400==0);
        }
        void print(){
            cout<<year<<"."<<month<<"."<<day;
        }
        private:
        int year,month,day;//数据成员
};
int main(){
    Date today;
    Date*P_DATE;
    P_DATE=&today;//把对象的地址赋值给指针P_DATE

    //如果使用Date创造一个函数实例，参数为：Date&d，当返回临时对象时不会改变d本身；若返回引用则会改变d本身
}