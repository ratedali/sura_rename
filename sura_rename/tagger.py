"""
Provides functions to tag Holy Quran Suras files
"""
from os import curdir
from os.path import join
from mutagen.easyid3 import EasyID3
from mutagen import MutagenError

def tag_files(files_to_titles, files_to_numbers, reciter, album=None, directory=curdir):
    """
    tags the files from dictionary with the corresponding
    title and assigns the same reciter and album to them

    also assigns the corresponding tracknumber from the
    flies_to_number dict

    if album is not given, the reciter's name is also used
    as album.
    the directory specifies the parent directory of the files
    """
    for curfile in files_to_titles:
        fulpath = join(directory, curfile)
        try:
            metadata = EasyID3(fulpath)
        except MutagenError:
            continue
        metadata['title'] = files_to_titles[curfile]
        metadata['artist'] = reciter
        metadata['album'] = album if album is not None else reciter
        metadata['tracknumber'] = "%d/114" % files_to_numbers[curfile]
        metadata.save()
