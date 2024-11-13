import cv2
import os, shutil
import json

OUTPUT_PATH = "output/cut/images"
analytic_output = {"images" : []}

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
# TODO Add padding to the image so that the last image is not cut off
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
    for i in range(0, height, crop_size):
        for j in range(0, width, crop_size):
            # Define the coordinates of the cropped image
            x1, y1 = j, i
            x2, y2 = j + crop_size, i + crop_size
            # Crop the image
            cropped_image = image[y1:y2, x1:x2]
            padded_image = pad_image(cropped_image, crop_size)
            # Save the cropped image in an output folder
            path = f"{OUTPUT_PATH}/{imagename}_{i}_{j}.jpg"
            analytic_output["images"].append(path)
            cv2.imwrite(path, padded_image)
    print("Image cropped successfully")

    for i in range(128, height, crop_size):
        for j in range(0, width, crop_size):
            # Define the coordinates of the cropped image
            x1, y1 = j, i
            x2, y2 = j + crop_size, i + crop_size
            # Crop the image
            cropped_image = image[y1:y2, x1:x2]
            padded_image = pad_image(cropped_image, crop_size)
            # Save the cropped image in an output folder

            path = f"{OUTPUT_PATH}/{imagename}_{i}_{j}.jpg"
            analytic_output["images"].append(path)
            cv2.imwrite(path, padded_image)

# Write a function that saves the analytics output to output/crop/analytics.json
def save_analytics(analytic_output):
    with open(f"output/cut/analytics.json", "w") as f:
        json.dump(analytic_output, f)

crop_image("screenshot.jpg")
cut_image("m.jpg", analytic_output)
save_analytics(analytic_output)