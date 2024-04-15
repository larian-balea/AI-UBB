#include <iostream>
#include <fstream>
#include <cassert>
#include "image_processing.h"
#include "drawing.h"

/// Prints
void printMenu() {
    std::cout << "0. Exit \n";
    std::cout << "1. Brightness and contrast adjustments \n";
    std::cout << "2. Gamma correction \n";
    std::cout << "3. Convolutions \n";
    std::cout << "4. Draw a shape: - circle \n";
    std::cout << "                             - line \n";
    std::cout << "                             - rectangle \n\n";
    std::cout << "Choose an option: ";
}
void printKernel() {
    std::cout << "1. Identity kernel \n";
    std::cout << "2. Mean blur kernel \n";
    std::cout << "3. 3x3 Gaussian blur kernel \n";
    std::cout << "4. Horizontal Sobel kernel \n";
    std::cout << "5. Vertical Sobel kernel \n\n";
    std::cout << "Choose a kernel: ";
}
void printShapes() {
    std::cout << "0. Exit \n";
    std::cout << "1. Circle \n";
    std::cout << "2. Line \n";
    std::cout << "3. Rectangle \n\n";
    std::cout << "Choose a shape: ";
}

/// Choose
int chooseOption() {
    int option;
    while (true) {
        std::cin >> option;
        if (option < 0 || option > 6) {
            std::cout << "The option must be an integer between 0 and 6!\n\n";
            std::cout << "Choose an option: ";
        } else
            return option;
    }
}
int chooseGain() {
    while (true) {
        std::cout << "Please introduce a value greater than 0 for the gain: ";
        int alpha;
        std::cin >> alpha;
        if (alpha <= 0)
            std::cout << "The gain must be greater than 0!\n\n";
        else
            return alpha;
    }
}
int chooseKernel() {
    int k;
    while (true) {
        std::cin >> k;
        if (k < 1 || k > 5) {
            std::cout << "The kernel must be an integer between 1 and 5!\n\n";
            std::cout << "Choose a kernel: ";
        } else
            return k;
    }
}
int chooseShape() {
    int shape;
    while (true) {
        std::cin >> shape;
        if (shape < 0 || shape > 3) {
            std::cout << "The shape must be an integer between 1 and 3!\n\n";
            std::cout << "Choose a shape: ";
        } else
            return shape;
    }
}

/// Kernels
//int identity(int x) {
//    return x;
//}
//int meanBlur(int x) {
//    return 1 / 9 * x;
//}
//int gaussianBlur(int x) {
//    return 1 / 16 * x;
//}
//int horizontalSobel(int x) {
//    return 1 / 4 * x;
//}
//int verticalSobel(int x) {
//    return 1 / 4 * x;
//}

/// Scale function
int ScaleFunction(int x) {
    if (x < 0)
        return 0;
    if (x > 255)
        return 255;
    return x;
}

// Function to process brightness and contrast adjustments
void processBrightnessAndContrast(Image& image, Image& result) {
    int alpha = chooseGain();
    int beta;
    std::cout << "Please introduce a value for the bias: ";
    std::cin >> beta;
    BrightnessAndContrastAdjustment b(alpha, beta);
    b.process(image, result);
    std::cout << "HOPA";
    result.save("photo.pgm");
    image = result;
    std::cout << "\n\n";
}

// Function to process gamma correction
void processGammaCorrection(Image& image, Image& result) {
    double gamma;
    std::cout << "Please introduce a value for the gamma: ";
    std::cin >> gamma;
    GammaCorrection g(gamma);
    g.process(image, result);

    result.save("photo.pgm");
    image = result;
    std::cout << "\n\n";
}

// Function to process convolutions
void processConvolutions(Image& image, Image& result) {
    printKernel();
    Image kernel(3, 3);
    int k = chooseKernel();
    switch (k) { /// Kernels
        case 1: { /// Identity kernel
            int ker[3][3] = {{0, 0, 0},
                                     {0, 1, 0},
                                     {0, 0, 0}};
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    kernel.at(i, j) = ker[i][j];
            break;
        }
        case 2: { /// Mean blur kernel
            int ker[3][3] = {{1, 1, 1},
                                     {1, 1, 1},
                                     {1, 1, 1}};
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    kernel.at(i, j) = ker[i][j];
            break;
        }
        case 3: { /// 3x3 Gaussian blur kernel
            int ker[3][3] = {{1, 2, 1},
                                     {2, 4, 2},
                                     {1, 2, 1}};
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    kernel.at(i, j) = ker[i][j];
            break;
        }
        case 4: { /// Horizontal Sobel kernel
            int ker[3][3] = {{1, 2, 1},
                                     {0, 0, 0},
                                     {-1, -2, -1}};
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    kernel.at(i, j) = ker[i][j];
            break;
        }
        case 5: { /// Vertical Sobel kernel
            int ker[3][3] = {{-1, 0, 1},
                                     {-2, 0, 2},
                                     {-1, 0, 1}};
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    kernel.at(i, j) = ker[i][j];
            break;
        }
        default:
            break;
    }
    Convolution c(kernel, ScaleFunction);
    c.process(image, result);
    std::cout << "HOPA? \n\n";

    result.save("photo.pgm");
    image = result;
    std::cout << "\n\n";
}

void drawCircle(Image& result){
    std::cout << "x coordinate for the center for the circle: ";
    int x;
    std::cin >> x;
    std::cout << "y coordinate for the center for the circle: ";
    int y;
    std::cin >> y;
    Point center(x, y);
    std::cout << "value for the radius of the circle: ";
    int radius;
    std::cin >> radius;
    std::cout << "value between 0 and 255 for the color of the circle: ";
    int color;
    std::cin >> color;
    drawCircle(result, center, radius, color);
}

void drawLine(Image& result){
    std::cout << "x coordinate for the first point: ";
    int x;
    std::cin >> x;
    std::cout << "y coordinate for the first point: ";
    int y;
    std::cin >> y;
    Point point1(x, y);
    std::cout << "x coordinate for the second point: ";
    std::cin >> x;
    std::cout << "y coordinate for the second point: ";
    std::cin >> y;
    Point point2(x, y);
    std::cout << "value between 0 and 255 for the color of the line: ";
    int color;
    std::cin >> color;
    drawLine(result, point1, point2, color);
}

void drawRectangle1(Image& result){
    std::cout << "Please introduce the x coordinate of the top-left point: ";
    int x;
    std::cin >> x;
    std::cout << "Please introduce the y coordinate of the top-left point: ";
    int y;
    std::cin >> y;
    int width, height;
    std::cout << "Introduce the value for width: ";
    std::cin >> width;
    std::cout << "Introduce the value for height: ";
    std::cin >> height;
    std::cout << "Please introduce a value between 0 and 255 for the color of the rectangle: ";
    int color;
    std::cin >> color;
    Rectangle rectangle(x, y, width, height);
    drawRectangle(result, rectangle, color);
}

void drawRectangle2(Image& result){
    std::cout << "Please introduce the x coordinate of the top-left point: ";
    int x;
    std::cin >> x;
    std::cout << "Please introduce the y coordinate of the top-left point: ";
    int y;
    std::cin >> y;
    Point topLeft(x, y);
    std::cout << "Please introduce the x coordinate of the right-bottom point: ";
    std::cin >> x;
    std::cout << "Please introduce the y coordinate of the right-bottom point: ";
    std::cin >> y;
    Point bottomRight(x, y);
    std::cout << "Please introduce a value between 0 and 255 for the color of the rectangle: ";
    int color;
    std::cin >> color;
    drawRectangle(result, topLeft, bottomRight, color);
}

void drawShape(Image& image, Image& result){
    printShapes();
    int shape = chooseShape();
    result = image;
    switch(shape) {
        case 1:
            drawCircle(result);
            break;
        case 2:
            drawLine(result);
            break;
        case 3: {

            std::cout << "1. Coordinates of the top-left corner and the width and height of the rectangle\n";
            std::cout << "2. Coordinates of the top-left and right-bottom points of the rectangle\n";
            int answer;
            std::cin >> answer;
            switch (answer) {
                case 1:
                    drawRectangle1(result);
                    break;
                case 2:
                    drawRectangle2(result);
                    break;
                default:
                    break;
            }
            break;
        }
        default:
            break;
    }

    result.save("photo.pgm");
    image = result;
    std::cout << "\n\n";
}

void run() {
    std::ifstream fin("mona.pgm");
    std::ofstream fout("photo.pgm");

    Image image(250, 360);
    image.load("mona.pgm");

    Image result(250, 360);
    while (true) {
        printMenu();
        int option = chooseOption();
        if (option == 0)
            break;
        switch (option) {
            case 1:
                processBrightnessAndContrast(image, result);
                break;
            case 2:
                processGammaCorrection(image, result);
                break;
            case 3:
                processConvolutions(image, result);
                break;
            case 4:
                drawShape(image, result);
                break;
            default:
                std::cout << "Invalid option!\n\n";
        }
    }
}

void test_size() {
    Size s1;
    Size s2(3, 4);
    assert(s1.getWidth() == 0);
    assert(s1.getHeight() == 0);
    assert(s2.getWidth() == 3);
    assert(s2.getHeight() == 4);
    s1.setWidth(5);
    s1.setHeight(6);
    assert(s1.getWidth() == 5);
    assert(s1.getHeight() == 6);
    assert(s1 == s1);
    assert(s2 < s1);
    assert(s2 <= s1);
    assert(s1 > s2);
    assert(s1 >= s2);
    assert(s1 != s2);
    std::cout << "Size tests passed!\n";
}
void test_point() {
    Point p1;
    Point p2(3, 4);
    assert(p1.getX() == 0);
    assert(p1.getY() == 0);
    assert(p2.getX() == 3);
    assert(p2.getY() == 4);
    p1.setX(5);
    p1.setY(6);
    assert(p1.getX() == 5);
    assert(p1.getY() == 6);
    assert(p2.getX() == 3);
    assert(p2.getY() == 4);
    std::cout << "Point tests passed!\n";
}
void test_rectangle() {
    Rectangle r1;
    Rectangle r2(1, 1, 2, 2);
    assert(r1.getX() == 0);
    assert(r1.getY() == 0);
    assert(r1.getWidth() == 0);
    assert(r1.getHeight() == 0);
    assert(r2.getX() == 1);
    assert(r2.getY() == 1);
    assert(r2.getWidth() == 2);
    assert(r2.getHeight() == 2);
    r2.setX(2);
    r2.setY(2);
    r1.setWidth(2);
    r1.setHeight(2);
    assert(r2.getX() == 2);
    assert(r2.getY() == 2);
    assert(r1.getWidth() == 2);
    assert(r1.getHeight() == 2);
    Rectangle r3 = r1 - Point(1, 1);
    assert(r3.getX() == -1);
    assert(r3.getY() == -1);
    r3 = r1 + Point(1, 1);
    assert(r3.getX() == 1);
    assert(r3.getY() == 1);
    r2 = r1 & r3;
    assert(r2.getX() == 1);
    assert(r2.getY() == 0);
    assert(r2.getWidth() == 1);
    assert(r2.getHeight() == 1);
    r2 = r1 | r3;
    assert(r2.getX() == 0);
    assert(r2.getY() == 1);
    assert(r2.getWidth() == 3);
    assert(r2.getHeight() == 3);
    std::cout << "Rectangle tests passed!\n";
}
void test_image() {
    Image i1;
    Image i2(3, 3);
    assert(i1.isEmpty());
    assert(!i2.isEmpty());
    assert(i1.getWidth() == 0);
    assert(i1.getHeight() == 0);
    assert(i2.getWidth() == 3);
    assert(i2.getHeight() == 3);
    auto **data = new unsigned char*[3];
    for (int i = 0; i < 3; i++) {
        data[i] = new unsigned char[3];
        for (int j = 0; j < 3; j++)
            data[i][j] = i+j;
    }
    i1.setWidth(3);
    i1.setHeight(3);
    i1.setData(data);
    assert(i1.getData() == data);
    assert(i1.at(1, 1) == 0);
    assert(i1.at(Point(1, 1)) == 0);
    assert(i1.row(1) == data[1]);
    assert(i1.size() == Size(3, 3));
    Image i3(i1);
    assert(i3.getData() == data);
    Image i4 = i1;
    assert(i4.getData() == data);
    i1.release();
    assert(i1.isEmpty());
    for (int i = 0; i < 3; i++) {
        delete[] data[i];
    }
    delete[] data;
    std::cout << "Image tests passed!\n";
}

void test_all() {
    test_size();
    test_point();
    test_rectangle();
    test_image();
    std::cout << "All tests passed!\n";
}

/// Main
int main() {
    int a(0);
    a += 1;
    int b{0};
    b += 2;
    int c = 0;
    c += 3;
    std::printf("%d %d %d\n\n", a, b, c);

    ///test_all();
    run();
    return 0;
}