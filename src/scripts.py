"""General helper functions.
"""
import os
import shutil
import logging
import fs
from pathlib import Path
from zipfile import ZipFile


LOG_FORMAT = '%(asctime)s - %(message)s'

logging.basicConfig(filename="cli_debug.log",
                    filemode='w',
                    format=LOG_FORMAT,
                    level=logging.DEBUG)

logger = logging.getLogger()



def is_directory(dir_path):
    """Checks if path is a directory.
    Parameters:
        path (str): The path to test
    Returns:
        bool : true if path is a directory or false if not.
    """
    isdir = os.path.isdir(dir_path)
    logger.debug("Path specified %s", dir_path)
    return isdir


def get_files(directory, filters="**/"):
    """ Grab Files in a specified path.
    
    Parameters:
        directory (str): The directory to grab files from
        filters (str)all : specify the types of files to grab. wildcards accepted
        (default will grab everything)
    Returns:
        all the files in directory as a generator. if the path is  not a valid directory
        None will be returned
    """
    if Path(directory).exists() and is_directory(directory):
        files = Path(directory).glob(filters)
        for file in files:
            yield file
    else:
        return None


def unzip_folder(zip_folder_path, target_folder=os.getcwd()):
    zip_file = ZipFile(zip_folder_path, 'r')
    zip_file.extractall(target_folder)
    zip_file.close()

def unzip_folders(zip_folder_path, target_folder=os.getcwd()):
    zipfiles = get_files(zip_folder_path, "**/*.zip")
    for file_item in zipfiles:
        unzip_folder(file_item)


def copy_file(source, target=os.getcwd()):
    if(is_directory(source)):
        fs.permissions.Permissions.create(0o700)
        shutil.copy(source, target)

def copy_files(source, target=os.getcwd(), filters="**/"):

    if(is_directory(source)):
        print("starting")
        files = get_files(source, filters)
        for file_item in files:
            copy_file(file_item, target)


def move_file(source, target=os.getcwd()):
    if(is_directory(source)):
            fs.permissions.Permissions.create(0o700)
            shutil.move(source, target)

def move_files(source, target=os.getcwd(), filters="**/"):
    if (is_directory(source)):
        files = get_files(source, filters)
        for file_item in files:
            move_file(file_item, target)

