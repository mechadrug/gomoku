#include<iostream>
using namespace std;

const int STACK_SIZE=100;
class stack3{
    public://对外接口
        stack3();
        void push(int e);
        void pop (int &e);
    private://隐藏的内容
        int buffer[STACK_SIZE];
        int top;
};

//外部接口的实现
void stack3::push(int e){
    if(top==STACK_SIZE-1){
        cout<<"overflow.\n";
        exit(-1);
    }
    top++;buffer[top]=e;
    return;
}

void stack3::pop(int &e){
    if(top == -1){
        cout<<"stack is empty.\n";
        exit(-1);
    }
    e=buffer[top];
    top--;
    return;
}

stack3::stack3(){
    top=-1;
}
int main(){
    stack3 st;
    int x;
    st.push(12);
    st.pop(x);
    //只能进行上述操作
    //st.top++;:会显示成员不可访问
}