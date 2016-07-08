"""
Provides functions to rename quran sura files
"""

from os.path import split, splitext, join
from os import rename

from .utils import get_mp3_files

def rename_in_dir(directory, names, name_only=False):
    """
    Renames all sura files in a given directory
    gets the new names from the provided dict
    name_only specifies whether to include numbers or not
    """
    for curfile in get_mp3_files(directory):
        parent, curname = split(curfile)
        index = splitext(curname)[0]
        basename = names[curname]
        newname = "%s%s.mp3" % (
            '' if name_only else str(index)+' - ', basename)
        newname = join(parent, newname)
        try:
            rename(curfile, newname)
        except FileNotFoundError:
            continue
