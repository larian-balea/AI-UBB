//
// Created by Larian on 4/2/2024.
//

#include "size.h"

/// Constructors

Size::Size() {
    width = 0;
    height = 0;
}

Size::Size(unsigned int width, unsigned int height) {
    this->width = width;
    this->height = height;
}

/// Getters

unsigned int Size::getWidth() const {
    return width;
}

unsigned int Size::getHeight() const {
    return height;
}

/// Setters

void Size::setWidth(unsigned int otherWidth) {
    this->width = otherWidth;
}

void Size::setHeight(unsigned int otherHeight) {
    this->height = otherHeight;
}

/// Operators overloading

bool Size::operator==(const Size &other) const {
    return width * height == other.width * other.height;
}

bool Size::operator<(const Size &other) const {
    return width * height < other.width * other.height;
}

bool Size::operator<=(const Size &other) const {
    return width * height <= other.width * other.height;
}

bool Size::operator>(const Size &other) const {
    return width * height > other.width * other.height;
}

bool Size::operator>=(const Size &other) const {
    return width * height >= other.width * other.height;
}

bool Size::operator!=(const Size &other) const {
    return width * height != other.width * other.height;
}