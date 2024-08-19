//
// Created by Larian on 4/2/2024.
//

#pragma once
#include "point.h"

class Rectangle{
private:
    int x, y;
    unsigned int width, height;

public:
    /// Constructors
    Rectangle();
    Rectangle(int x, int y, unsigned int width, unsigned int height);

    /// Getters
    [[nodiscard]] int getX() const;
    [[nodiscard]] int getY() const;
    [[nodiscard]] unsigned int getWidth() const;
    [[nodiscard]] unsigned int getHeight() const;

    /// Setters
    void setX(int myX);
    void setY(int myY);
    void setWidth(unsigned int myWidth);
    void setHeight(unsigned int myHeight);

    /// Operators overloading
    Rectangle operator+(const Point& otherPoint) const;
    Rectangle operator-(const Point& otherPoint) const;

    friend Rectangle operator&(const Rectangle& rect1, const Rectangle& rect2);
    friend Rectangle operator|(const Rectangle& rect1, const Rectangle& rect2);

};
