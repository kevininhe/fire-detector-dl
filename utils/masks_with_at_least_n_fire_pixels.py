"""This scripts count the white pixels in a mask and if it has more pixels than NUM_PIXELS the mask path is printed.
It can be use to find images and/or masks with a minimal amount of fire pixels.
"""

import os
import sys
from glob import glob
import numpy as np
import rasterio
import shutil

#MASK_PATH = '../../dataset/groundtruth/manual_annotation'
MASK_PATH = '/Users/kevininfante/Library/CloudStorage/OneDrive-UniversidaddelosAndes/Universidad_de_Los_Andes/2022-20/DeepLearning/Proyecto/dataset/masks/intersection'
PATCH_PATH = '/Users/kevininfante/Library/CloudStorage/OneDrive-UniversidaddelosAndes/Universidad_de_Los_Andes/2022-20/DeepLearning/Proyecto/dataset/images/patches'
CONTINENTE = 'Oceania'
SAVE_IMAGE = '/Users/kevininfante/Library/CloudStorage/OneDrive-UniversidaddelosAndes/Universidad_de_Los_Andes/2022-20/DeepLearning/Proyecto/ImagenesFuego/{}/Imagenes'.format(CONTINENTE)
SAVE_METADATA = '/Users/kevininfante/Library/CloudStorage/OneDrive-UniversidaddelosAndes/Universidad_de_Los_Andes/2022-20/DeepLearning/Proyecto/ImagenesFuego/{}/Metadata'.format(CONTINENTE)
METADATA_PATH = '/Users/kevininfante/Downloads/Oceania'
NUM_PIXELS = 300
"""
    Possible values:
    - intersection
    - voting
    - Kumar-Roy (patches)
    - Murphy (patches)
    - Schroeder (patches)
"""
CALCULATION_ALG = 'intersection'

def get_mask_arr(path):
    """ Abre a mascara como array"""
    with rasterio.open(path) as src:
        img = src.read().transpose((1, 2, 0))
        seg = np.array(img, dtype=int)

        return seg[:, :, 0]

def copy_patch_to_folder(maskPath):
    mask_name = os.path.basename(maskPath)
    # Get patch
    patch_name = mask_name.replace('{}_'.format(CALCULATION_ALG),'')
    # Get patch path
    patch_path = os.path.join(PATCH_PATH,patch_name)
    if os.path.exists(patch_path):
        dest_path = os.path.join(SAVE_IMAGE,patch_name)
        # Copy image
        shutil.copyfile(patch_path, dest_path)
    else:
        print('El archivo no existe: {}'.format(patch_path))

def copy_metadata_to_folder(maskPath):
    mask_name = os.path.basename(maskPath)
    # Get zone
    zone = mask_name.split('_')[2]
    zoneZipFile = 'z{}.zip'.format(zone)
    zoneZipFilePath = os.path.join(METADATA_PATH,zoneZipFile)
    if os.path.exists(zoneZipFilePath):
        dest_path = os.path.join(SAVE_METADATA,zoneZipFile)
        # Copy ZIP
        shutil.copyfile(zoneZipFilePath, dest_path)
    else:
        print('El archivo zip no existe: {}'.format(zoneZipFilePath))

if __name__ == '__main__':


    images_path = glob(os.path.join(MASK_PATH, '*.tif'))
    print('Mask Path: {}'.format(MASK_PATH))
    print('Total images found: {}'.format( len(images_path) ))
    num_images = 0
    for image_path in images_path:
        mask = get_mask_arr(image_path)

        count = (mask > 0).sum()

        if count > NUM_PIXELS:
            print('# Fire Pixels: {} - Image: {}'.format(count, image_path))
            copy_patch_to_folder(image_path)
            copy_metadata_to_folder(image_path)
            num_images += 1

    print('Num. images: {}'.format(num_images))
