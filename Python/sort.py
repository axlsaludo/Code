import os
import shutil
from pathlib import Path

def get_file_type(file_name):
    """Returns the file type based on the file extension."""
    return file_name.split('.')[-1]

def create_directory(path):
    """Creates a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def move_file(file_path, target_directory):
    """Moves a file to the target directory, renaming if a file with the same name exists."""
    create_directory(target_directory)
    file_name = os.path.basename(file_path)
    destination = os.path.join(target_directory, file_name)
    
    # Check if file already exists and rename
    base, extension = os.path.splitext(destination)
    counter = 1
    while os.path.exists(destination):
        destination = f"{base}_{counter}{extension}"
        counter += 1
    
    shutil.move(file_path, destination)

def auto_sort_files(source_directory, target_directories):
    """Sorts files by type and moves them to specified directories, including subfolders."""
    for root, _, files in os.walk(source_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_type = get_file_type(file).lower()
            target_directory = target_directories.get(file_type, target_directories['default'])
            move_file(file_path, target_directory)
    
    # Delete empty directories
    for root, dirs, _ in os.walk(source_directory, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)
            except OSError as e:
                print(f"Error: {dir_path} : {e.strerror}")

if __name__ == "__main__":
    source_directory = r"C:\Users\ewanm\Downloads\com.adobe.lrmobile"  # Replace with the source directory path
    target_directories = {
        'jpg': r"C:\Users\ewanm\Downloads\Files\Images",  # Replace with the target directory for images
        'png': r"C:\Users\ewanm\Downloads\Files\Images",  # Replace with the target directory for images
        'pdf': r"C:\Users\ewanm\Downloads\Files\Documents",  # Replace with the target directory for documents
        'txt': r"C:\Users\ewanm\Downloads\Files\Texts",  # Replace with the target directory for text files
        'default': r"C:\Users\ewanm\Downloads\Files\Others"  # Replace with the target directory for other files
    }

    auto_sort_files(source_directory, target_directories)
