//
// Created by Larian on 4/3/2024.
//

#pragma once
#include "Image.h"

class ImageProcessing {
public:
    virtual void process(const Image& src, Image& dst);
};

class BrightnessAndContrastAdjustment : public ImageProcessing {
private:
    unsigned int gain;
    int bias;
public:
    BrightnessAndContrastAdjustment();
    BrightnessAndContrastAdjustment(unsigned int gain, int bias);
    void process(const Image& src, Image& dst) override;
};

class GammaCorrection : public ImageProcessing {
private:
    double gamma;
public:
    GammaCorrection();
    explicit GammaCorrection(double gamma);
    void process(const Image& src, Image& dst) override;
};

class Convolution : public ImageProcessing {
private:
    Image kernel;
    int (*scaleFunction)(int);
public:
    Convolution();
    Convolution(const Image& kernel, int (*scaleFunction)(int));
    void process(const Image& src, Image& dst) override;
};
