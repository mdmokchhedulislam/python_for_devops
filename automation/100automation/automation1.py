
# Project 1: File Organizer (File Management Automation)

# Automatically organize files in a specified directory based on their file extensions.

# Functional Requirements

# The script must accept a directory path as input.

# It must scan all files in the given directory.

# It must detect each file's extension.

# It must create a folder named after the file extension if it does not already exist.

# It must move files into their respective extension-based folders.

# It must process only files (ignore subdirectories).

# Non-Functional Requirements

# Must be compatible with Python 3.

# Must work on Linux and Windows systems.

# Should handle large numbers of files efficiently.

# Expected Outcome

# All files in the target directory will be automatically organized into folders based on their extensions, improving directory structure and maintainability.


import os
import shutil


def organized_files(directory):
    if not os.path.exists(directory):
        print("directory does't exist")
        return
    for filename in os.listdir(directory):
        file_path=os.path.join(directory, filename)

        if os.path.isfile(file_path):
            if "." in filename:
                ext = filename.split(".")[-1].lower()
            else:
                ext = "no extension"
        
        folder_path = os.path.join(directory, ext)

        if not os.path.exists(folder_path):
            os.mkdirs(folder_path)
        
        destination = os.path.join(folder_path, filename)

        try:
            shutil.move(file_path, destination)
            print(f"Moved: {filename} → {ext}/")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

    print("\nFile organization completed successfully!")