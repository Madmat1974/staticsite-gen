import os, shutil
from textnode import *

import os, shutil

def copy_file_function(source, destination):
    items = os.listdir(source)
    
    for item in items:
        full_source_path = os.path.join(source, item)
        full_destination_path = os.path.join(destination, item)
        print(f"Full destination path: {full_destination_path}")

        if os.path.isfile(full_source_path):
            shutil.copy(full_source_path, full_destination_path)
            print(f"copying {item} from {source} to {destination}")
        else:
            os.mkdir(full_destination_path)
            print("making directory")
            copy_file_function(full_source_path, full_destination_path)

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    copy_file_function("static", "public")

main()