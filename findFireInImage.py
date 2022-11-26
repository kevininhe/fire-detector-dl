from modelManager.models import *
from modelManager.generator import *
import os
import cv2
from imageUtilities import normalize_arr

# from models import *
IMAGE_NAME = 'LC08_L1TP_099069_20200827_20200827_01_RT_p00819.tif'

IMAGE_PATH = './inputImage'
OUTPUT_PATH = './outputImage'

# 0 or 1
CUDA_DEVICE = 0

# 10 or 3
N_CHANNELS = 10
# 16 or 64
N_FILTERS = 64

MASK_ALGORITHM = 'Intersection'
MODEL_NAME = 'unet'
IMAGE_SIZE = (256, 256)
TH_FIRE = 0.25

# ajusta o nome da pasta que estão os pesos
MODEL_FOLDER_NAME = 'kumar-roy' if MASK_ALGORITHM == 'Kumar-Roy' else MASK_ALGORITHM
MODEL_FOLDER_NAME = 'intersection' if MASK_ALGORITHM == 'Intersection' else MASK_ALGORITHM
ARCHITECTURE = '{}_{}f_2conv_{}'.format( MODEL_NAME, N_FILTERS, '10c' if N_CHANNELS == 10 else '762' )

WEIGHTS_FILE = './weights/model_{}_{}_final_weights.h5'.format(MODEL_NAME, MASK_ALGORITHM)

print(ARCHITECTURE)
print(WEIGHTS_FILE)

def findFireInImage(imageName,npArrayImage,outputPath,weightsFile):
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    os.environ["CUDA_VISIBLE_DEVICES"] = str(CUDA_DEVICE)
    model = get_model(MODEL_NAME, input_height=IMAGE_SIZE[0], input_width=IMAGE_SIZE[1], n_filters=N_FILTERS, n_channels=N_CHANNELS)
    model.summary()

    print('Loading weights...')
    model.load_weights(weightsFile)
    print('Weights Loaded')

    img = normalize_arr(npArrayImage)

    y_pred = model.predict(np.array( [img] ), batch_size=1)
    y_pred = y_pred[0, :, :, 0] > TH_FIRE

    y_pred = np.array(y_pred * 255, dtype=np.uint8)

    output_image_name = imageName.replace('.tif','.png')
    output_image = os.path.join(outputPath, output_image_name)
    #cv2.imwrite(output_image, cv2.cvtColor(y_pred, cv2.COLOR_RGB2BGR))
    return cv2.cvtColor(y_pred, cv2.COLOR_RGB2BGR)
