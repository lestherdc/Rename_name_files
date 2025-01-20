""""This program is intented to change
the names of the file in a folder with the same
name was made to save time"""

import os

def rename_files_in_folder(folder_name, new_base_name, extension):
    try:
        # Get the absolute path of the folder
        folder_path = os.path.abspath(folder_name)

        if not os.path.exists(folder_path):
            print(f"Error: Folder'{folder_name}' does not exist.")
            return

        # List all files in the folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        if not files:
            print(f"No files found in folder '{folder_name}'.")
            return

        #Rename files
        counter = 1
        for file_name in files:
            old_path = os.path.join(folder_path, file_name)
            new_name = f"{new_base_name}{counter}.{extension}"
            new_path = os.path.join(folder_path,new_name)

            os.rename(old_path, new_path)
            counter +=1

        print(f"Renamed {counter -1} files in the folder '{folder_name}'.")
    except Exception as e:
        print(f"An error ecorred: {e}")

if __name__ == "__main__":
    folder_name = input("Enter the folder name: ")
    new_base_name = input("Enter the new base name for files: ")
    extension = input("Enter the new file extension: ")

    rename_files_in_folder(folder_name, new_base_name, extension)