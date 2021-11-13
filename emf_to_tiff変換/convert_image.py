import os 
import glob
from PIL import Image

raw_data_path = "./raw_data/"
converted_data_path = "./converted_data/"

files = sorted((glob.glob(raw_data_path+"/*.out")))
filenames = []
for file in files:
    filenames.append(os.path.splitext(os.path.basename(file))[0])

for filename in filenames:
  Image.open(raw_data_path+filename+".emf").save(converted_data_path+filename+".tiff",quality=90)