import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

def get_picture_filenames_from_folder(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith(".png")]

def load_and_transform_pictures(filenames, folder_path):
    pictures = []
    for filename in filenames:
        picture = cv2.imread(os.path.join(folder_path, filename))
        picture = picture/255 # Pixels between 0 and 1
        pictures.append(picture)
    return np.array(pictures)

def display_blur_sharp_and_pred_images(img_id, blur_list, sharp_list, pred_list):
    listed = [blur_list, pred_list, sharp_list]
    for l in listed:
        plt.imshow(l[img_id])
        plt.show()
        
def calc_mae(image1, image2):
    mae = np.mean(np.abs((image1 - image2))) # Calculate pixel differences
    return mae

def calc_mse(image1, image2):
    mse = np.mean((image1.astype("float") - image2.astype("float")) ** 2) 
    return mse

def load_picture_from_folder(filename, file_path):
    picture = cv2.imread(os.path.join(file_path, filename))
    return picture/255 # Pixels between 0 and 1


