//
// Created by Larian on 4/2/2024.
//

#pragma once
#include <string>
#include <fstream>
#include "rectangle.h"
#include "size.h"

class Image{
private:
    unsigned char** m_data;
    unsigned int m_width;
    unsigned int m_height;

public:
    /// Constructors
    Image();
    Image(unsigned int w, unsigned int h);

    /// Release memory
    void release();

    /// Rule of 3
    Image(const Image &other);
    Image& operator=(const Image &other);
    ~Image();

    /// Getters
    [[nodiscard]] unsigned char** getData() const;
    [[nodiscard]] unsigned int getWidth() const;
    [[nodiscard]] unsigned int getHeight() const;
    [[nodiscard]] Size size() const;

    [[nodiscard]] bool isEmpty() const;

    [[nodiscard]] unsigned char& at(unsigned int x, unsigned int y) const;
    [[nodiscard]] unsigned char& at(Point pt) const;
    [[nodiscard]] unsigned char* row(int y) const;

    /// Setters
    void setData(unsigned char** data);
    void setWidth(unsigned int width);
    void setHeight(unsigned int height);

    /// Read and Write
    friend std::ostream& operator<<(std::ostream& os, const Image& dt);
    friend std::istream& operator>>(std::istream& is, Image& dt);

    /// Load and Save
    bool load(const std::string& imagePath);
    bool save(const std::string& imagePath) const;

    /// Operator overloading
    Image operator+(const Image &i) const;
    Image operator-(const Image &i) const;
    Image operator*(double s) const;

    /// Image operations
    bool getROI(Image &roiImg, Rectangle roiRect) const;
    bool getROI(Image &roiImg, unsigned int x, unsigned int y, unsigned int width, unsigned int height) const;

    /// Static methods
    static Image zeros(unsigned int width, unsigned int height);
    static Image ones(unsigned int width, unsigned int height);
};
