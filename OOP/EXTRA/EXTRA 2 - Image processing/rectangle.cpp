//
// Created by Larian on 4/2/2024.
//

#include "rectangle.h"
#include <algorithm>
/// Constructors

Rectangle::Rectangle() {
    x = 0;
    y = 0;
    width = 0;
    height = 0;
}

Rectangle::Rectangle(int x, int y, unsigned int width, unsigned int height) {
    this->x = x;
    this->y = y;
    this->width = width;
    this->height = height;
}

/// Getters

int Rectangle::getX() const {
    return x;
}

int Rectangle::getY() const {
    return y;
}

unsigned int Rectangle::getWidth() const {
    return width;
}

unsigned int Rectangle::getHeight() const {
    return height;
}

/// Setters

void Rectangle::setX(int myX) {
    this->x = myX;
}

void Rectangle::setY(int myY) {
    this->y = myY;
}

void Rectangle::setWidth(unsigned int myWidth) {
    this->width = myWidth;
}

void Rectangle::setHeight(unsigned int myHeight) {
    this->height = myHeight;
}

/// Operators overloading

Rectangle Rectangle::operator+(const Point &otherPoint) const {
    return {x+otherPoint.getX(), y+otherPoint.getY(), width, height};
}

Rectangle Rectangle::operator-(const Point &otherPoint) const {
    return {x-otherPoint.getX(), y-otherPoint.getY(), width, height};
}

Rectangle operator&(const Rectangle &rect1, const Rectangle &rect2) {
    int x1 = rect1.getX();
    int y1 = rect1.getY();
    unsigned int w1 = rect1.getWidth();
    unsigned int h1= rect1.getHeight();
    int x2 = rect2.getX();
    int y2 = rect2.getY();
    unsigned int w2 = rect2.getWidth();
    unsigned int h2 = rect2.getHeight();

    int x = std::max(x1, x2); // cea mai din dreapta latura din stanga
    int y = std::min(y1, y2); // cea mai de jos latura de sus
    unsigned int width = std::min(x1 + w1, x2 + w2) - x; // cea mai din stanga latura din dreapta - x
    unsigned int height = y - std::max(y1 - h1, y2 - h2); // y - cea mai de sus latura de jos

    return {x, y, width, height};
}

Rectangle operator|(const Rectangle &rect1, const Rectangle &rect2) {
    int x1 = rect1.getX();
    int y1 = rect1.getY();
    unsigned int w1 = rect1.getWidth();
    unsigned int h1= rect1.getHeight();
    int x2 = rect2.getX();
    int y2 = rect2.getY();
    unsigned int w2 = rect2.getWidth();
    unsigned int h2 = rect2.getHeight();

    int x = std::min(x1, x2);
    int y = std::max(y1, y2);
    unsigned int w = std::max(x1 + w1, x2 + w2) - x;
    unsigned int h = y - std::min(y1 - h1, y2 - h2);

    return {x, y, w, h};
}














