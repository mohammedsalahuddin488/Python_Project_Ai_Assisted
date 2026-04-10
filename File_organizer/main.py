import os
import shutil

FOLDER_PATH = os.getcwd()

# File type mapping
FILE_TYPE_MAPPING = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.js', '.html', '.css'],
    'Others': []
}

#creat a file if not exist
for folder in FILE_TYPE_MAPPING:
    if not os.path.exists(folder):
        os.mkdir(folder)

# Organize files
for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

    if os.path.isfile(file_path): # Only process files, skip directories    
        file_ext = os.path.splitext(file)[1].lower()
        moved = False
        #don't arrange the main.py file
# if file != 'main.py':

        for folder, extensions in FILE_TYPE_MAPPING.items():# Check if the file extension matches any in the mapping    
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))
                print(f"Moved: {file} → {folder}")
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(FOLDER_PATH, 'Others', file))


            
            print(f"Moved: {file} → Others")