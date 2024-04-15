//
// Created by Larian on 4/2/2024.
//

#pragma once

class Size{
private:
    unsigned int width, height;

public:
    /// Constructors
    Size();
    Size(unsigned int width, unsigned int height);

    /// Getters
    [[nodiscard]] unsigned int getWidth() const;
    [[nodiscard]] unsigned int getHeight() const;

    /// Setters
    void setWidth(unsigned int otherWidth);
    void setHeight(unsigned int otherHeight);

    /// Operators
    bool operator==(const Size& other) const;
    bool operator<(const Size& other) const;
    bool operator<=(const Size& other) const;
    bool operator>(const Size& other) const;
    bool operator>=(const Size& other) const;
    bool operator!=(const Size& other) const;
};