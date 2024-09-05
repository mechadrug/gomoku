#include <iostream>
#include<vector>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    
    // 使用基于范围的for循环遍历数组
    for (int num : arr) {
        std::cout << num << " ";
    }

    std::vector<int> vec = {10, 20, 30, 40, 50};
    
    // 使用基于范围的for循环遍历vector
    for (int num : vec) {
        std::cout << num << " ";
    }

    // 使用引用遍历，修改vector中的元素
    for (int& num : vec) {
        num += 5;
    }
    //引用可以提高效率
    // 再次遍历，输出修改后的值
    for (int num : vec) {
        std::cout << num << " ";
    }

    return 0;
}
//适用范围：数组；标准库容器；自定义类型自定义类型：只要实现了 begin() 和 end() 函数，或者适配了 std::begin 和 std::end 函数，你也可以使用基于范围的 for 循环遍历这些类型。