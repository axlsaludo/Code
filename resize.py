import os
from PIL import Image

# Function to resize images in a specified folder
def resize_images_in_folder(folder_path, target_size=(28, 28)):
    # Loop through all files in the folder and subfolders
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):  # Supported image types
                image_path = os.path.join(root, filename)
                
                try:
                    # Open the image
                    img = Image.open(image_path)

                    # Convert image to grayscale if not already
                    if img.mode != 'L':
                        img = img.convert('L')

                    # Resize the image to the target size (28x28) without specifying resampling
                    img_resized = img.resize(target_size)

                    # Save the resized image, overwrite the original file
                    img_resized.save(image_path)

                    print(f"Resized and saved: {image_path}")

                except Exception as e:
                    print(f"Error processing {image_path}: {e}")

    print("Done resizing all images.")

# Ask the user for the folder path
folder_path = input(r"C:\Users\ewanm\Documents\MATLAB\neuralnetwork\LettersAndNumbers\Y")

# Call the function with the specified folder path
resize_images_in_folder(folder_path)
