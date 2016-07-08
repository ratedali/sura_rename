"""
Provides utilities for the sura_rename package
"""

import os.path

def prepend_path(file_list, path):
    """
    Returns an iterable with each element replaced with a prepended path
    """
    return (os.path.join(path, file) for file in file_list)

def get_ext_files(directory, ext):
    """
    returns an iterable containing only files ending in ext
    assumes ext is in ASCII
    """
    allfiles = (file for file in prepend_path(os.listdir(directory), directory))
    return (file for file in allfiles if os.path.splitext(file)[1].lower() == ext.lower())

def get_mp3_files(directory):
    """
    Returns an iterable with all the mp3 files in the given directory with absoulute paths
    """
    return get_ext_files(directory, '.mp3')
