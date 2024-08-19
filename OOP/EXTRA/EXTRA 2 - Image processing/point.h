//
// Created by Larian on 4/2/2024.
//

#pragma once

class Point {
private:
    int x, y;

public:
    // Constructors
    Point();
    Point(int x, int y);

    // Getters
    [[nodiscard]] int getX() const;
    [[nodiscard]] int getY() const;

    // Setters
    void setX(int otherX);
    void setY(int otherY);
};
