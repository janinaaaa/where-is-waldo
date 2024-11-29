import cv2
import os, shutil
import json
from timeit import default_timer as timer

OUTPUT_PATH = "output/cut/images"
analytic_output = {"cut" : {"images": []}}

# Function to crop the image
def crop_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Resize the image
    image = cv2.resize(image, (256, 256))
    # Save the image
    cv2.imwrite(image_path, image)
    print("Image cropped successfully")

def pad_image(image, size):
    height, width, _ = image.shape
    if height < size or width < size:
        padded_image = cv2.copyMakeBorder(image, 0, size - height, 0, size - width, cv2.BORDER_CONSTANT, value=[0, 0, 0])
        return padded_image
    return image



# write a fuction that takes an image and cuts in it smaller images of size 256x256
# TODO Function to set the images together to form the original image
def cut_image(image_path, analytic_output):
    # Delete output folder if it exists
    try:
        shutil.rmtree(OUTPUT_PATH)
    except:
        pass

    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
        
    # Read the image
    image = cv2.imread(image_path)
    # Get the dimensions of the image
    height, width, _ = image.shape
    # Define the size of the cropped images
    crop_size = 256
    imagename = image_path.split(".")[0]
    # Loop over the image and crop it into smaller images
    cut(0, analytic_output, image, height, width, crop_size, imagename)
    cut(128, analytic_output, image, height, width, crop_size, imagename)
    print("Image cropped successfully")

def cut(offset, analytic_output, image, height, width, crop_size, imagename):
    for i in range(offset, height, crop_size):
        for j in range(0, width, crop_size):
            crop_time_start = timer()
            # Define the coordinates of the cropped image
            x1, y1 = j, i
            x2, y2 = j + crop_size, i + crop_size
            # Crop the image
            cropped_image = image[y1:y2, x1:x2]
            padded_image = pad_image(cropped_image, crop_size)
            # Save the cropped image in an output folder
            path = f"{OUTPUT_PATH}/{imagename}_{i}_{j}.jpg"
            cv2.imwrite(path, padded_image)
            crop_time_end = timer()
            single_image_crop_time = crop_time_end - crop_time_start
            data = {"path": path, "time": single_image_crop_time}
            analytic_output["cut"]["images"].append(data)

# Write a function that saves the analytics output to output/crop/analytics.json
def save_analytics(analytic_output):
    with open(f"output/cut/analytics.json", "w") as f:
        json.dump(analytic_output, f)

start = timer()
cut_image("departmentstore.jpg", analytic_output)
end = timer()

time = end - start
analytic_output["time"] = time # Time taken in seconds
save_analytics(analytic_output)