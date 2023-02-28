from PIL import Image
import os
from tqdm import tqdm

input_dir = "data"  # directory to search for images
output_format = input("Enter output format (e.g. png, jpg): ")  # format to convert images to

num_files = 0
for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith((".dib", ".gif", ".icns", ".ico", ".im", ".jpeg", ".jfif", ".msp", ".pcx", ".png", ".ppm", ".sgi", ".spider", ".tga", ".tiff", ".webp", ".xbm", ".xvthumb", ".jpg", ".bmp", ".png", ".gif", ".tiff", ".webp")) and not file.endswith(output_format):
            num_files += 1

with tqdm(total=num_files) as pbar:
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith((".dib", ".gif", ".icns", ".ico", ".im", ".jpeg", ".jfif", ".msp", ".pcx", ".png", ".ppm", ".sgi", ".spider", ".tga", ".tiff", ".webp", ".xbm", ".xvthumb", ".jpg", ".bmp", ".png", ".gif", ".tiff", ".webp")) and not file.endswith(output_format):
                # open the image and convert to the desired format
                with Image.open(os.path.join(root, file)) as img:
                    output_filename = os.path.splitext(file)[0] + f".{output_format}"
                    # save the new image to the same directory as the original file
                    img.save(os.path.join(root, output_filename))
                # delete the original file
                os.remove(os.path.join(root, file))
                pbar.update(1)