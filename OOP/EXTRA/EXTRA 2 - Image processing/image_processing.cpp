//
// Created by Larian on 4/3/2024.
//

#include <valarray>
#include <iostream>
#include "image_processing.h"

void ImageProcessing::process(const Image &src, Image &dst) {
    for(unsigned int i{0}; i < src.getHeight(); i++)
        for(unsigned int j{0}; j < src.getWidth(); j++)
            dst.at(i, j) = src.at(i, j);
}

BrightnessAndContrastAdjustment::BrightnessAndContrastAdjustment() {
    gain = 1;
    bias = 0;
}

BrightnessAndContrastAdjustment::BrightnessAndContrastAdjustment(unsigned int gain, int bias) {
    this->gain = gain;
    this->bias = bias;
}

void BrightnessAndContrastAdjustment::process(const Image &src, Image &dst) {
    for(unsigned int i{0}; i < src.getHeight(); i++)
        for(unsigned int j{0}; j < src.getWidth(); j++) {
            int value = (int)gain * src.at(i, j) + bias;
            if (value < 0)
                dst.at(i, j) = 0;
            else if (value > 255)
                dst.at(i, j) = 255;
            else
                dst.at(i, j) = value;
        }
}

GammaCorrection::GammaCorrection() {
    gamma = 1.0;
}

GammaCorrection::GammaCorrection(double gamma) {
    this->gamma = gamma;
}

void GammaCorrection::process(const Image &src, Image &dst) {
    for(unsigned int i{0}; i < src.getHeight(); i++)
        for(unsigned int j{0}; j < src.getWidth(); j++) {
            int value = (int)(std::pow(src.at(i, j), gamma));
            if (value < 0)
                dst.at(i, j) = 0;
            else if (value > 255)
                dst.at(i, j) = 255;
            else
                dst.at(i, j) = value;
        }
}

Convolution::Convolution() {
    kernel = Image();
    scaleFunction = [](int x) -> int {return x;};
}

Convolution::Convolution(const Image &kernel, int (*scaleFunction)(int)) {
    this->kernel = kernel;
    this->scaleFunction = scaleFunction;
}

void Convolution::process(const Image &src, Image &dst) {
    for(int i{0}; i < src.getHeight() - kernel.getHeight(); i++)
        for(int j{0}; j < src.getWidth() - kernel.getWidth(); j++) {
            Image aux(kernel.getWidth(), kernel.getHeight());
            src.getROI(aux, i, j, kernel.getWidth(), kernel.getHeight());
            int value = 0;
            for(int k{0}; k < kernel.getHeight(); k++)
                for(int l{0}; l < kernel.getWidth(); l++) {
                    value += aux.at(k, l) * kernel.at(k, l);
                }
            dst.at(i, j) = (unsigned char)scaleFunction(value);
        }
}

