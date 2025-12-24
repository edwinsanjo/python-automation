import platform
from pathlib import Path

downloads = Path.home() / "Downloads"
images_folder = downloads / "Media"
documents_folder = downloads / "Documents"
installers_folder = downloads / "Installers"
code_folder = downloads / "Codes"
archive_folder = downloads / "Archives"

if images_folder.is_dir() == False:
    images_folder.mkdir()
    print("Creating Folder Media.\n\n")
if documents_folder.is_dir() == False:
    documents_folder.mkdir()
    print("Creating Folder pdf.\n\n")
if archive_folder.is_dir() == False:
    archive_folder.mkdir()
    print("Creating Folder Archives.\n\n")
if code_folder.is_dir() == False:
    code_folder.mkdir()
    print("Creating Folder Archives.\n\n")
if installers_folder.is_dir() == False:
    installers_folder.mkdir()
    print("Creating Folder Installers.\n\n")


for item in downloads.iterdir():
    d = item.name.split(".")

    # Media - Images / Videos / Audios
    if d[-1] == "jpg" or d[-1] == "png" or d[-1] == "jpeg":
        print(item.name + "moved to images folder")
        item.rename(images_folder/item.name)
    elif d[-1] == "mp4" or d[-1] == "mov" or d[-1] == "mkv":
        print(item.name + "moved to images folder")
        item.rename(images_folder/item.name)
    elif d[-1] == "mp3" or d[-1] == "wav" or d[-1] == "m4a":
        print(item.name + "moved to images folder")
        item.rename(images_folder/item.name)

    # Documents
    elif d[-1] == "pdf" or d[-1] == "doc" or d[-1] == "docx" or d[-1] == "ppt":
        print(item.name + "moved to images folder")
        item.rename(documents_folder/item.name)
    elif d[-1] == "pptx" or d[-1] == "xls" or d[-1] == "xlsx" or d[-1] == "txt":
        print(item.name + "moved to images folder")
        item.rename(documents_folder/item.name)

    # Installers
    elif d[-1] == "exe" or d[-1] == "msi" or d[-1] == "dmg" or d[-1] == "apk":
        print(item.name + "moved to Installers folder")
        item.rename(installers_folder/item.name)

    # codes
    elif d[-1] == "py" or d[-1] == "java" or d[-1] == "c" or d[-1] == "cpp":
        print(item.name + "moved to codes folder")
        item.rename(code_folder/item.name)
    elif d[-1] == "html" or d[-1] == "css" or d[-1] == "js" or d[-1] == "json":
        print(item.name + "moved to codes folder")
        item.rename(code_folder/item.name)
    elif d[-1] == "jsx" or d[-1] == "xml" or d[-1] == "tsx" or d[-1] == "ts":
        print(item.name + "moved to codes folder")
        item.rename(code_folder/item.name)

    # Archives
    elif d[-1] == "7z" or d[-1] == "zip" or d[-1] == "rar" or d[-1] == "gz" or d[-1] == "tar":
        print(item.name + "moved to Archives folder")
        item.rename(archive_folder/item.name) 
    elif d[-1] == "7z" or d[-1] == "tgz" or d[-1] == "xz":
        print(item.name + "moved to Archives folder")
        item.rename(archive_folder/item.name) 


