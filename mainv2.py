""""This program is intented to change
the names of the file in a folder with the same
name was made to save time"""

"""#Specially when you made your own image dataset and need
    normalize the name of the dataset"""

import os

def rename_files_in_folder(folder_name, extension):
    try:
        # Get the absolute path of the folder
        folder_path = os.path.abspath(folder_name)
        print(f"{folder_path}")
        if not os.path.exists(folder_path):
            print(f"Error: Folder'{folder_name}' does not exist.")
            return

        # List all files in the folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        if not files:
            print(f"No files found in folder '{folder_name}'.")
            return

        #Get just the name of the folder in case is a path
        name_folder = os.path.basename(folder_path)

        #Rename files with the same folder name
        counter = 1
        for file_name in files:
            old_path = os.path.join(folder_path, file_name)
            new_name = f"{name_folder}{counter}.{extension}"
            new_path = os.path.join(folder_path,new_name)

            os.rename(old_path, new_path)
            counter +=1

        print(f"Renamed {counter -1} files in the folder '{folder_name}'.")
    except Exception as e:
        print(f"An error ecorred: {e}")

if __name__ == "__main__":
    folder_name = input("Enter the folder name: ")
    extension = input("Enter the new file extension: ")

    rename_files_in_folder(folder_name, extension)