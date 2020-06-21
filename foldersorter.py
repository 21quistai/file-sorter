"""
This is to automatically clean up my projects folder that contains all my 
coding files and projects. files that are created in the projects folder will 
be automatically moved into a folder based on the language. This can also be 
used to organize other folders.
"""
import os
import shutil
import time

directory = "/Users/21quistai/" + raw_input("What folder do you want to sort? ")
os.chdir(directory)
CURRENT_DIR = os.getcwd()
file_dir = ""
DIRS = ["Audio/", "Images/", "Videos/", "Code/","Zip/", "Other/"]

AUDIO_EXTENSIONS = [".mp3", ".pcm", ".wav", ".aiff", ".aac", "ogg", ".wma", 
        ".flac", ".alac"]
IMAGE_EXTENSIONS = [".jpeg", ".jpg", ".png", ".gif", ".webp", ".tiff", ".raw", ".psd",
        ".bpm", ".heif", ".indd", ".svg"]
VIDEO_EXTENSIONS = []
CODE_EXTENSIONS = []
ZIP_EXTENSIONS = [".zip"]


def make_directories():
    try:
        for file in DIRS:
            os.mkdir(file)
            print("Made new folder: %s"%(file))
    except OSError:
        print("File already exists")

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) and file[0] != ".":
            yield file

def move_files():
    for file in files(CURRENT_DIR):
        ext =  "." + file.split(".")[-1]
        file_dir = CURRENT_DIR + "/" + file
        file_destination = CURRENT_DIR + "/Other"
        if ext in IMAGE_EXTENSIONS:
            file_destination = CURRENT_DIR + "/Images"
            print("hi")
        elif ext in ZIP_EXTENSIONS:
            file_destination = CURRENT_DIR + "/Zip"
        elif ext in AUDIO_EXTENSIONS:
            file_destination = CURRENT_DIR + "/Audio"
        elif ext in VIDEO_EXTENSIONS:
            file_destination = CURRENT_DIR + "/Video"
        elif ext in CODE_EXTENSIONS:
            file_destination = CURRENT_DIR + "/Code"
        shutil.move(file, file_destination)


def run():
	print("Cleaning up Downloads")
	make_directories()
	move_files()

run()


