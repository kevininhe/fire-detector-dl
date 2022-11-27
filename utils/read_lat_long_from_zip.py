from zipfile import ZipFile
import os
import re
import csv

METADATA_ZIP = '/Users/kevininfante/Library/CloudStorage/OneDrive-UniversidaddelosAndes/Universidad_de_Los_Andes/2022-20/DeepLearning/Proyecto/ImagenesFuego/Oceania/Metadata'
OUT_PATH = '/Users/kevininfante/Library/CloudStorage/OneDrive-UniversidaddelosAndes/Universidad_de_Los_Andes/2022-20/DeepLearning/Proyecto/WebAnalizadorIncendio/img_lat_lon.csv'
dict_locations = dict()
for filename in os.listdir(METADATA_ZIP):
    f = os.path.join(METADATA_ZIP, filename)
    with ZipFile(f, 'r') as zip:
        with zip.open(zip.infolist()[0],"r") as myfile:
            lat_lon = [None] * 2
            for line in myfile:
                if 'CORNER_UL_LAT_PRODUCT'.encode() in line:
                    lat = re.findall("\d+\.\d+", line.decode("utf-8"))
                    if len(lat) > 0:
                        lat_lon[0] = lat[0]
                elif 'CORNER_UL_LON_PRODUCT'.encode() in line:
                    lon = re.findall("\d+\.\d+", line.decode("utf-8"))
                    if len(lon) > 0:
                        lat_lon[1] = lon[0]
            dict_locations[filename.replace('.zip','').replace('z','')] = lat_lon

print(dict_locations)
# Escribir las ubicaciones en archivo csv
open_mode = 'a+' if os.path.exists(OUT_PATH) else 'w+'
with open(OUT_PATH,open_mode) as f:
    w = csv.writer(f)
    if open_mode == 'w+':
        w.writerow(['zone','latitude','longitude'])
    for zone,lat_lon in dict_locations.items():
        row = []
        row.append(zone)
        row = row + lat_lon
        w.writerow(row)

    
#CORNER_UL_LAT_PRODUCT = -13.40840
#CORNER_UL_LON_PRODUCT = 129.02863