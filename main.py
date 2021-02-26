__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'


# In main.py, write the following functions:
import os
import shutil
import zipfile


# 1. clean_cache: takes no arguments and creates an empty folder named cache
# in the current directory. If it already exists, it deletes everything in the
# cache folder.
def clean_cache(dir='cache'):
    if os.path.exists(dir):
        for root, dirs, files in os.walk(dir):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                shutil.rmtree(os.path.join(root, name))
    else:
        try:
            os.mkdir(dir)
        except OSError:
            print(f'Failed writing directory {dir}')


# 2. cache_zip: takes a zip file path (str) and a cache dir path (str) as
# arguments, in that order. The function then unpacks the indicated zip file
# into a clean cache folder. You can test this with data.zip file.
def cache_zip(zip_dir_file: str, cache_dir: str):
    if os.path.exists(zip_dir_file):
        clean_cache(cache_dir)
        with zipfile.ZipFile(zip_dir_file, 'r') as zip_ref:  # reading the file
            zip_ref.extractall(cache_dir)  # unpacking the zip-file
    else:
        print(f'Failed finding directory {zip_dir_file}')


# 3. cached_files: takes no arguments and returns a list of all the files in
# the cache. The file paths should be specified in absolute terms. Search the
# web for what this means! No folders should be included in the list. You do
# not have to account for files within folders within the cache directory.
def cached_files():
    file_list = []
    for root, dirs, files in os.walk(os.path.abspath(os.curdir+'\\cache')):
        for name in files:
            if root[-6:] == '\\cache':  # exclude files in subfolders
                file_list.append(os.path.join(root, name))
    return file_list


# 4. find_password: takes the list of file paths from cached_files as an
# argument. This function should read the text in each one to see if the
# password is in there. Surely there should be a word in there to incidicate
# the presence of the password? Once found, find_password should return this
# password string.
def find_password(file_list=(cached_files())):
    for cached_file in file_list:
        with open(cached_file) as f:
            lines = f.readlines()
        for line in lines:
            if 'password:' in line:
                return line.replace('password:','').strip()
                break
            else:
                continue
