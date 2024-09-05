#include<iostream>
using namespace std;

const int STACK_SIZE=100;
struct stack1
{
    /* data */
    int buffer[STACK_SIZE];//存放栈元素
    int top;//栈顶位置
};

int main(){
    stack1 st;//定义栈数据
    st.top=-1;//对st进行初始化，表示top目前在栈顶，可以压入SIZE个元素

    int num=12;//样例数据

    if(st.top==STACK_SIZE-1){
        cout<<"Stack is overflow.\n";exit(-1);
    }
    st.top++;
    st.buffer[st.top]=num;
    //遵循后进先出规则.

    //退栈则检测st.top==-1
}
//存在的问题：操作要知道数据的具体表示形式；操作不通用；麻烦且容易误写