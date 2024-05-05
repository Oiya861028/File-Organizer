from os import listdir
from os.path import isfile, join
import os
import shutil

file_path='C:/Users/yubin/Downloads'
folders = [f for f in listdir(file_path)]
i = 1
for folder in folders:
    current_folder = file_path+'/'+folder
    files = [f for f in listdir(current_folder)]
    for file in files:
        file_dir = current_folder+'/'+file
        shutil.move(file_dir, file_path)
        print(i," - ", file_dir+">>>"+file_path)
