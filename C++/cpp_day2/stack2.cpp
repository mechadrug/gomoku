#include<iostream>
using namespace std;

const int STACK_SIZE=100;
struct stack2
{
    /* data */
    int buffer[STACK_SIZE];//存放栈元素
    int top;//栈顶位置
};

void push(stack2 &s,int e){
    if(s.top==STACK_SIZE-1){
        cout<<"overflow.\n";
        exit(-1);
    }
    s.top++;s.buffer[s.top]=e;
    return;
}
void pop(stack2 &s,int &e){
    if(s.top==-1){
        cout<<"empty.\n";
        exit(-1);
    }
    e= s.buffer[s.top];s.top--;
    return;
}
void init(stack2 &s){
    s.top = -1;
}
int main(){
    stack2 st;
    int x;
    init(st);
    push(st,12);
    pop(st,x);//退栈并且将原来栈顶的元素存入变量x
}
//仍然存在的问题：1.需要手动创建栈（main函数内部）2.存在“病毒函数”如f(stack2 &s)
//可以对栈造成破坏