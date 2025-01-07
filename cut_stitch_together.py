# Stitch multiple images together and combine the Bounding Boxes

OUTPUT_PATH = "output/cut"
IMPUT_IMAGES_PATH = "output/cut/images"

def stitch_images(image_paths, output_path):
    images = [cv2.imread(image_path) for image_path in image_paths]
    # Get the dimensions of the images
    height, width, _ = images[0].shape
    # Create a blank image
    combined_image = np.zeros((height * 2, width * 2, 3), np.uint8)
    # Loop over the images and combine them
    combined_image[:height, :width] = images[0]
    combined_image[:height, width:] = images[1]
    combined_image[height:, :width] = images[2]
    combined_image[height:, width:] = images[3]
    # Save the combined image
    cv2.imwrite(output_path, combined_image)
    print("Images stitched together successfully")