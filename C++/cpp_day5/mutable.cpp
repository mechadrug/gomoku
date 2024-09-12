#include <iostream>
using namespace std;
 
int main()
{
   int m = 0;
   int n = 0;
   [&, n] (int a) mutable { m = ++n + a; }(4);//这里区别n++：n++的话m出来就是4而不是5了
   cout << m << endl << n << endl;
}