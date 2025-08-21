import os
import re

def find_files_with_pattern(path, my_pattern):
    all_dir = os.walk(path)
    for dirpath, dirnames, filenames in all_dir:
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_text = open(file_path)
            check = re.search(my_pattern, file_text.read())
            if check:
                print(f"Pattern found in: {filename}\nat {dirpath}\nand Matched Text: {check.group()}")
                print("*******************************************")
            else:
                pass
            file_text.close()