"""
Provides utilities for the sura_rename package
"""

from os import listdir
from os.path import join, splitext


def prepend_path(file_list, path):
    """
    Returns an iterable with each element replaced with a prepended path
    """
    return (join(path, file) for file in file_list)


def get_ext_files(d, ext):
    """
    returns an iterable containing only files ending in ext
    assumes ext is in ASCII
    """
    allfiles = (file for file in prepend_path(listdir(d), d))

    def has_ext(f, x):
        return splitext(f)[1].lower() == x.lower()

    return (file for file in allfiles if has_ext(file, ext))


def get_mp3_files(directory):
    """
    Returns an iterable with all the mp3 files in the given directory
    with absoulute paths
    """
    return get_ext_files(directory, '.mp3')
