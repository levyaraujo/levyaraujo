import os
# importação dos módulos necessários
import pathlib
import glob
import shutil

local = pathlib.Path('/mnt/d/Downloads/') # definição do caminho em que a função deve procurar os arquivos

def search(extension):
    os.chdir(local)
    new_folder = os.mkdir(f'{extension}')
    for file in os.listdir(local):
        if f'{extension}' in file:
            shutil.copy(f'{local}/{file}', f'{new_folder}/{file}')
        

search('exe')