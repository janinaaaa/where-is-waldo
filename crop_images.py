import cv2
import os, shutil

OUTPUT_PATH = "output/cropped_images"

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
def cut_image(image_path):
    # Delete output folder if it exists
    try:
        shutil.rmtree(OUTPUT_PATH)
    except:
        pass

    # Check if output folder exists else create it
    if not os.path.exists("output"):
        os.mkdir("output")
    if not os.path.exists(OUTPUT_PATH):
        os.mkdir(OUTPUT_PATH)
        
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

            cv2.imwrite(f"{OUTPUT_PATH}/{imagename}{i}_{j}.jpg", padded_image)
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


            cv2.imwrite(f"{OUTPUT_PATH}/{imagename}_offset_{i}_{j}.jpg", padded_image)

crop_image("screenshot.jpg")
cut_image("m.jpg")