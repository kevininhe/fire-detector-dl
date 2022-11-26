from findFireInImage import findFireInImage
from imageUtilities import convertRasterToRGB
import cv2
import numpy as np
import rasterio
import tifffile
import os

image_name = 'LC08_L1TP_099069_20200827_20200827_01_RT_p00819.tif'
input_path = './inputImage'
output_path = './outputImage'
weights_file = './weights/model_unet_Intersection_final_weights.h5'

output_path_conv = './inputImageConverted'

#findFireInImage(image_name,input_path,output_path,weights_file)
#convertRasterToRGB(image_name,input_path,output_path_conv)

def decode_image(img, name):
    image = cv2.imdecode(
        np.frombuffer(img, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    path = f"inputImage/{name}"
    cv2.imwrite(path, image)
    return path


# Veamos el output de leer una imagen TIF
def usingRaster(path):
    img = rasterio.open(path).read((7,6,2)).transpose((1, 2, 0))
    #img = rasterio.open(path).read().transpose(1, 2, 0)
    print(img.dtype)
    print(img.shape)
    print(img)
    return img

def usingTiff(path):
    img = tifffile.imread(path)
    print(img.dtype)
    print(img.shape)
    img_2 = img.reshape(-1)
    print(img_2.shape)
    print(img_2)
    return img

def RGBTiff(path):
    inputImage = tifffile.imread(path)
    get_img_dim7 = inputImage[:,:,6].reshape(256,256,1)
    get_img_dim6 = inputImage[:,:,5].reshape(256,256,1)
    get_img_dim2 = inputImage[:,:,1].reshape(256,256,1)
    three_dim_img = np.concatenate((get_img_dim7,get_img_dim6,get_img_dim2),axis=-1)

    print(three_dim_img.dtype)
    print(three_dim_img.shape)
    print(three_dim_img)
    return three_dim_img

# Image to be read with Raster
pathKI = "/Users/kevininfante/Library/CloudStorage/OneDrive-UniversidaddelosAndes/Universidad_de_Los_Andes/2022-20/DeepLearning/Proyecto/WebAnalizadorIncendio/inputImage"
imName = "LC08_L1TP_099069_20200827_20200827_01_RT_p00819.tif"
img_path = os.path.join(pathKI, imName)
print('Using Raster')
rst_img = usingRaster(img_path)

pathKI = "/Users/kevininfante/Library/CloudStorage/OneDrive-UniversidaddelosAndes/Universidad_de_Los_Andes/2022-20/DeepLearning/Proyecto/WebAnalizadorIncendio/webInputImage"
imName = "LC08_L1TP_099069_20200827_20200827_01_RT_p00819.tif"
img_path = os.path.join(pathKI, imName)
print('Using Tiff')
tiff_img = RGBTiff(img_path)

print("¿Son iguales?")
print((rst_img==tiff_img).all())
