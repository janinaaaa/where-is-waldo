import cv2


# Function to crop the image
def crop_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Resize the image
    image = cv2.resize(image, (256, 256))
    # Save the image
    cv2.imwrite(image_path, image)
    print("Image cropped successfully")
