import sys
import os
from PIL import Image

#grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check is new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through Pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0]  # removes .jpg
    img.save(f'{output_folder}/{clean_name}.png', 'png')#convert images to png
    print('all done!')

