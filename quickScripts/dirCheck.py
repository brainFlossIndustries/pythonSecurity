import os

def check_accessible_folders(base_path):
    accessible_folders = []
    
    for root, dirs, files in os.walk(base_path, topdown=True):
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            if os.access(dir_path, os.R_OK):  # Check read access
                accessible_folders.append(dir_path)
    
    return accessible_folders

base_directory = "/"  # Start from root or change to a specific directory
accessible_dirs = check_accessible_folders(base_directory)

for d in accessible_dirs:
    print(d)
