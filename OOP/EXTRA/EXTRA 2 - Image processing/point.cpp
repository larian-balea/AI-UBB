//
// Created by Larian on 4/2/2024.
//

#include "point.h"

/// Constructors

Point::Point() {
    x = 0;
    y = 0;
}

Point::Point(int x, int y) {
    this->x = x;
    this->y = y;
}

/// Getters

int Point::getX() const {
    return x;
}

int Point::getY() const {
    return y;
}

/// Setters

void Point::setX(int otherX) {
    x = otherX;
}

void Point::setY(int otherY) {
    y = otherY;
}