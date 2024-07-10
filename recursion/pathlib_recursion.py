import os
from pathlib import Path

parent_folder_path = Path('.')
os.mkdir('dist')
dist  = Path('path_to_save_files') or Path('dist')
def parse_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            print(f"Parse folder: This is folder - {element.name}")
            parse_folder(element)
        if element.is_file():
            print(f"Parse folder: This is file - {element.name}")

parse_folder(parent_folder_path)