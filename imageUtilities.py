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
        
def convertRasterToRGB(inputImage):
    # Se obtienen las dimensiones 7,6 y 2 de la imagen, y se concatenan
    get_img_dim7 = inputImage[:,:,6].reshape(256,256,1)
    get_img_dim6 = inputImage[:,:,5].reshape(256,256,1)
    get_img_dim2 = inputImage[:,:,1].reshape(256,256,1)
    three_dim_img = np.concatenate((get_img_dim7,get_img_dim6,get_img_dim2),axis=-1)

    # Normalización y paso a escala RGB
    img = np.float32(three_dim_img)/MAX_PIXEL_VALUE
    img = np.array(img * 255, dtype=np.uint8)
    return img

def decode_image(img, name):
    image = np.frombuffer(img,dtype=np.uint16)
    image_reshaped = image[1239:].reshape(256,256,10)
    path = f"webInputImage/{name}"
    tifffile.imsave(path, image_reshaped)
    return path

def normalize_arr(img):
    img = np.float32(img)/MAX_PIXEL_VALUE
    return img