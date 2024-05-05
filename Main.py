from os import listdir
from os.path import isfile, join
import os
import shutil

file_path='C:/Users/yubin/OneDrive/DeskTop/Test'
files = [f for f in listdir(file_path) if isfile(join(file_path, f))]
file_type = []
file_dict = {}
for f in files:
    filetype = f.split(".")[1]
    if(filetype not in file_type):
        file_type.append(filetype)
        new_folder_location = file_path+'/'+filetype
        file_dict[str(filetype)] = new_folder_location
        if(os.path.exists(file_dict[filetype])):
            continue
        else:
            os.makedirs(new_folder_location)



