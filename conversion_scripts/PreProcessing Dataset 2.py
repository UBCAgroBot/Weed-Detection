import json
import os
import matplotlib.pyplot as plt
import shutil


input_path = r"C:\AgroBot\Dataset\weedcoco"
output_path = "C:/AgroBot/Dataset/test-data/"

f = open(os.path.join(input_path, '_annotations.coco.json'))
data = json.load(f)
f.close()

file_names = []

def load_images_from_folder(folder):
    count = 0

    # Ensure 'images' directory exists in 'Output'
    images_dir = os.path.join(output_path, 'test-images')
    os.makedirs(images_dir, exist_ok=True)

    for filename in os.listdir(folder):
        source = os.path.join(folder, filename)
        destination = os.path.join(images_dir, f"test-img{count}.jpg")

        try:
            shutil.copy(source, destination)
            print(f"File {filename} copied successfully.")
        except shutil.SameFileError:
            print("Source and destination represent the same file.")

        file_names.append(filename)
        count += 1
        
load_images_from_folder(os.path.join(input_path, 'test-images'))

def get_img_ann(image_id):
    img_ann = []
    isFound = False
    for ann in data['annotations']:
        if ann['image_id'] == image_id:
            img_ann.append(ann)
            isFound = True
    if isFound:
        return img_ann
    else:
        print(image_id)
        print("not found in annotations")
        return None
    
def get_img(filename):
    for img in data['images']:
        if img['file_name'] == filename:
            return img
    
count = 0

def create_labels_directory():
    # Ensure 'labels' directory exists in 'Output'
    labels_dir = os.path.join(output_path, 'test-labels')
    os.makedirs(labels_dir, exist_ok=True)

create_labels_directory()

for filename in file_names:
    # Extracting image 
    img = get_img(filename)
    img_id = img['id']
    img_w = img['width']
    img_h = img['height']

    # Get Annotations for this image
    img_ann = get_img_ann(img_id)

    if img_ann:
        # Opening file for the current image
        file_object = open(os.path.join(output_path, 'test-labels', f"test-img{count}.txt"), "a")

        for ann in img_ann:
            current_category =  1 #ann['category_id'] - 1 As YOLO format labels start from 0 
            current_bbox = ann['bbox']
            x = current_bbox[0]
            y = current_bbox[1]
            w = current_bbox[2]
            h = current_bbox[3]
      
            # Finding midpoints
            x_centre = (x + (x+w))/2
            y_centre = (y + (y+h))/2
      
            # Normalization
            x_centre = x_centre / img_w
            y_centre = y_centre / img_h
            w = w / img_w
            h = h / img_h
      
            # Limiting up to a fixed number of decimal places
            x_centre = format(x_centre, '.6f')
            y_centre = format(y_centre, '.6f')
            w = format(w, '.6f')
            h = format(h, '.6f')
          
            # Writing current object 
            file_object.write(f"{current_category} {x_centre} {y_centre} {w} {h}\n")

        file_object.close()
    count += 1  # This should be outside the if img_ann block.


