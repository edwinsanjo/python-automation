# import os
# import subprocess

# if platform.system() == 'Linux' :
#     folder_path = f"/home/{os.environ.get("USER")}/Documents"
#     subprocess.run(["xdg-open", folder_path])
#     print();



import platform
from pathlib import Path

downloads = Path.home() / "Downloads"
images_folder = downloads / "images"
pdf_folder = downloads / "pdfs"
installers_folder = downloads / "installers"

if images_folder.is_dir() == False:
    images_folder.mkdir()
    print("Creating Folder Images.\n\n")
if pdf_folder.is_dir() == False:
    pdf_folder.mkdir()
    print("Creating Folder pdf.\n\n")
if platform.system() == 'Windows' and installers_folder.is_dir() == False:
    installers_folder.mkdir()
    print("Creating Folder pdf.\n\n")


for item in downloads.iterdir():
    d = item.name.split(".")
    if d[-1] == "jpg" or d[-1] == "png" or d[-1] == "jpeg":
        print(item.name + "moved to images folder")
        item.rename(images_folder/item.name)
    elif d[-1] == "pdf":
        print(item.name + "moved to images folder")
        item.rename(pdf_folder/item.name)
    elif platform.system() == 'Windows' and d[-1] == "exe":
        print(item.name + "moved to images folder")
        item.rename(installers_folder/item.name)

    # print(d[-1])
    


