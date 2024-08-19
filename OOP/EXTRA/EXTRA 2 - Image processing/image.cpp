//
// Created by Larian on 4/2/2024.
//

#include <iostream>
#include "image.h"

/// Constructors
Image::Image() {
    m_data = nullptr;
    m_width = 0;
    m_height = 0;
}

Image::Image(unsigned int w, unsigned int h) {
    m_width = w;
    m_height = h;
    m_data = new unsigned char * [h];
    for (unsigned int i = 0; i < h; i++) {
        m_data[i] = new unsigned char[w];
        for(unsigned int j = 0; j < w; j++)
            m_data[i][j] = 0;
    }
}

/// Release memory
void Image::release() {
    if(m_data != nullptr) {
        for(unsigned int i{0}; i < m_height; i++)
            delete[] m_data[i];
        delete[] m_data;
        m_data = nullptr;
    }
}

/// Rule of three
Image::Image(const Image &other) {
    m_width = other.m_width;
    m_height = other.m_height;
    m_data = new unsigned char * [m_height];
    for(unsigned int i{0} ; i < m_height; i++) {
        m_data[i] = new unsigned char[m_width];
        for(unsigned int j{0}; j < m_width; j++)
            m_data[i][j] = other.m_data[i][j];
    }
}

Image& Image::operator=(const Image &other) {
    if(this != &other) {
        release();
        /// deep copy
        if (other.m_data != nullptr) {
            m_width = other.m_width;
            m_height = other.m_height;
            m_data = new unsigned char * [m_height];
            for(unsigned int i{0} ; i < m_height; i++) {
                m_data[i] = new unsigned char[m_width];
                for(unsigned int j{0}; j < m_width; j++)
                    m_data[i][j] = other.m_data[i][j];
            }
        }
    }
    return *this;
}

Image::~Image() {
    release();
}

/// Getters
unsigned char **Image::getData() const {
    return m_data;
}

unsigned int Image::getWidth() const {
    return m_width;
}

unsigned int Image::getHeight() const {
    return m_height;
}

Size Image::size() const {
    return {m_width, m_height};
}

bool Image::isEmpty() const {
    return m_data == nullptr && m_width == 0 && m_height == 0;
}

unsigned char &Image::at(Point pt) const {
    return m_data[pt.getX()][pt.getY()];
}

unsigned char &Image::at(unsigned int x, unsigned int y) const {
    return m_data[x][y];
}

unsigned char *Image::row(int y) const {
    return m_data[y];
}

/// Setters
void Image::setData(unsigned char **data) {
    for (unsigned int i{0}; i < m_height; i++)
        for (unsigned int j{0}; j < m_width; j++)
            m_data[i][j] = data[i][j];
}

void Image::setWidth(unsigned int width) {
    m_width = width;
}

void Image::setHeight(unsigned int height) {
    m_height = height;
}

/// Read and Write
std::ostream& operator<<(std::ostream& os, const Image& dt){
    os << "P2" << std::endl;
    os << "# Simple pgm image example" << std::endl;
    os << dt.m_width << " " << dt.m_height << std::endl;
    os << "255" << std::endl;
    for(unsigned int i{0}; i < dt.m_height; i++) {
        for(unsigned int j{0}; j < dt.m_width; j++)
            os << (int)dt.m_data[i][j] << " ";
        os << std::endl;
    }
    return os;
}

std::istream& operator>>(std::istream& is, Image& dt) {
    /// Read header
    std::string magic;
    std::getline(is, magic);
    if(magic != "P2")
        return is;

    /// Read comment
    std::string comment;
    std::getline(is, comment);

    /// Read width and height
    is >> dt.m_width >> dt.m_height;

    /// Read max value
    int maxVal;
    is >> maxVal;

    /// Read data
    dt.m_data = new unsigned char * [dt.m_height];
    for(unsigned int i{0}; i < dt.m_height; i++) {
        dt.m_data[i] = new unsigned char[dt.m_width];
        for(unsigned int j{0}; j < dt.m_width; j++) {
            int pixelValue;
            is >> pixelValue;
            dt.m_data[i][j] = static_cast<unsigned char>(pixelValue);
        }
    }
    return is;
}

/// Load and Save
bool Image::load(const std::string& imagePath) {
    std::ifstream file(imagePath);
    if(!file)
        return false;
    file >> *this;
    return true;
}

bool Image::save(const std::string& imagePath) const {
    std::ofstream file(imagePath);
    if(!file)
        return false;
    file << *this;
    return true;
}

/// Operator overloading
Image Image::operator+(const Image &i) const {
    if(i.getWidth() != m_width || i.getHeight() != m_height)
        throw std::invalid_argument("Images must have the same size");
    Image img(m_width, m_height);
    for(unsigned int y{0}; y < m_height; y++)
        for(unsigned int x{0}; x < m_width; x++)
            img.at(x, y) = at(x, y) + i.at(x, y);
    return img;
}

Image Image::operator-(const Image &i) const {
    if(i.getWidth() != m_width || i.getHeight() != m_height)
        throw std::invalid_argument("Images must have the same size");
    Image img(m_width, m_height);
    for(unsigned int y{0}; y < m_height; y++)
        for(unsigned int x{0}; x < m_width; x++)
            img.at(x, y) = at(x, y) - i.at(x, y);
    return img;
}

Image Image::operator*(double s) const {
    Image img(m_width, m_height);
    for(unsigned int y{0}; y < m_height; y++)
        for(unsigned int x{0}; x < m_width; x++)
            img.at(x, y) = static_cast<unsigned char>(at(x, y) * s);
    return img;
}

/// Image operations
bool Image::getROI(Image &roiImg, Rectangle roiRect) const {
    if(roiRect.getX() + roiRect.getWidth() >= m_width || roiRect.getY() + roiRect.getHeight() >= m_height)
        return false;
    roiImg.setWidth(roiRect.getWidth());
    roiImg.setHeight(roiRect.getHeight());
    roiImg.m_data = new unsigned char * [roiImg.m_height];
    for(unsigned int i{0}; i < roiImg.m_height; i++) {
        roiImg.m_data[i] = new unsigned char[roiImg.m_width];
        for(unsigned int j{0}; j < roiImg.m_width; j++)
            roiImg.m_data[i][j] = at(roiRect.getX() + j, roiRect.getY() + i);
    }
    return true;
}

bool Image::getROI(Image &roiImg, unsigned int x, unsigned int y, unsigned int width, unsigned int height) const {
    if(x + width >= m_width || y + height >= m_height)
        return false;
    roiImg.setWidth(width);
    roiImg.setHeight(height);
    roiImg.m_data = new unsigned char * [roiImg.m_height];
    for(unsigned int i{0}; i < roiImg.m_height; i++) {
        roiImg.m_data[i] = new unsigned char[roiImg.m_width];
        for(unsigned int j{0}; j < roiImg.m_width; j++)
            roiImg.m_data[i][j] = at(x + j, y + i);
    }
    return true;
}

/// Static methods
Image Image::zeros(unsigned int width, unsigned int height) {
    Image img(width, height);
    for(unsigned int i{0}; i < height; i++)
        for(unsigned int j{0}; j < width; j++)
            img.m_data[i][j] = 0;
    return img;
}

Image Image::ones(unsigned int width, unsigned int height) {
    Image img(width, height);
    for(unsigned int i{0}; i < height; i++)
        for(unsigned int j{0}; j < width; j++)
            img.m_data[i][j] = 1;
    return img;
}
