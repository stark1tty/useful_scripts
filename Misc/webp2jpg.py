# converts .webp images in a folder to .jpgs

import os
from PIL import Image

# Directory containing the .webp files
directory = r'PATH'

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.webp'):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        # Open the image file
        with Image.open(file_path) as img:
            # Define the new filename with the .jpg extension
            new_filename = os.path.splitext(file_path)[0] + '.jpg'
            # Save the image in JPG format
            img.convert('RGB').save(new_filename, 'jpeg')
        # Optionally, if you want to remove the original .webp file, uncomment the next line
        os.remove(file_path)

print("Conversion completed.")
