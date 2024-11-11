import cv2


# Extract images from a given video
def extract_images(video_path):
    # Read the video
    video = cv2.VideoCapture(video_path)
    # Initialize the frame count
    frame_count = 0
    # Loop through the video
    while True:
        # Read the frame
        ret, frame = video.read()
        # Break the loop if the frame is not read
        if not ret:
            break
        # Save the frame as an image
        cv2.imwrite(f"frame_{frame_count}.jpg", frame)
        # Increment the frame count
        frame_count += 1
    print(f"{frame_count} frames extracted successfully")
