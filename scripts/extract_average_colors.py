import cv2
import numpy as np

def extract_average_colors(video_path, output_image_path, frame_step=2):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    average_colors = []

    # Compute average colors
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % frame_step == 0:
            average_color = frame.mean(axis=0).mean(axis=0)
            average_colors.append(average_color)
        
        frame_count += 1

    cap.release()

    # Create an image from the average colors
    if average_colors:
        height = 100  # height of each color strip
        width = len(average_colors)  # total width of the image
        output_image = np.zeros((height, width, 3), dtype=np.uint8)

        for i, color in enumerate(average_colors):
            output_image[:, i] = color

        # Save the output image
        cv2.imwrite(output_image_path, output_image)

# Example
video_path = '../data/top_gun.mp4'
image_path = '../data/top_gun.png'
extract_average_colors(video_path, image_path)
