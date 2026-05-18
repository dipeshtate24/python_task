import os 

folder_path = os.listdir('Image_folder')
n = 1
for file in folder_path:
    if file.endswith((".png", ".jpg")):
        print(file)
        os.rename(f"Image_folder/{file}", f"Image_folder/{n}.png")
        n += 1
        