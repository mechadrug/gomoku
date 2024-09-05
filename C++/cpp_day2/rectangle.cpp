class Rectangle {
private:
    int width;
    int height;

public:
    // 构造函数
    Rectangle(int w, int h) : width(w), height(h) {}

    // 操作接口：计算面积
    int area() const {
        return width * height;
    }

    // 操作接口：设置宽和高
    void setDimensions(int w, int h) {
        width = w;
        height = h;
    }
};
