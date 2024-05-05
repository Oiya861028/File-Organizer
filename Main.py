from os import listdir
from os.path import isfile, join
import os
import shutil

file_path='C:/Users/yubin/Downloads'
files = [f for f in listdir(file_path) if isfile(join(file_path, f))]
file_type = []
file_dict = {}
for f in files:
    filetype = f.split(".")[-1]
    if(filetype not in file_type):
        file_type.append(filetype)
        new_folder_location = file_path+'/'+filetype
        file_dict[str(filetype)] = new_folder_location
        if(os.path.exists(file_dict[filetype])):
            continue
        else:
            os.makedirs(new_folder_location)
i = 1
for file in files:
    fileType = file.split(".")[-1]
    source = file_path+'/'+file
    if(fileType in file_dict.keys()):
        target = file_dict[str(fileType)]
        shutil.move(source, target)
        print(i," - ",source+">>>"+target)
    i+=1


