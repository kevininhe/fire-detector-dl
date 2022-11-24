import rasterio
import numpy as np
import os
import cv2
import tifffile

MAX_PIXEL_VALUE = 65535 # Max. pixel value, used to normalize the image

def get_img_762bands(path):
    img = rasterio.open(path).read((7,6,2)).transpose((1, 2, 0))    
    img = np.float32(img)/MAX_PIXEL_VALUE
    
    return img
        
def convertRasterToRGB(inputImage,inputPath,outputPath):
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    outputImageName = inputImage.replace('.tif','.png')
    inputImagePath = os.path.join(inputPath, inputImage)
    img = get_img_762bands(inputImagePath)

    img = np.array(img * 255, dtype=np.uint8)
    cv2.imwrite(os.path.join(outputPath, outputImageName), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

def decode_image(img, name):
    image = np.frombuffer(img,dtype=np.uint16)
    image_reshaped = image[1239:].reshape(256,256,10)
    path = f"webInputImage/{name}"
    tifffile.imsave(path, image_reshaped)
    return path

def normalize_arr(img):
    img = np.float32(img)/MAX_PIXEL_VALUE
    return img