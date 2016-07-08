"""
setup for quran_rename module
"""
import codecs
from os import path
from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

with codecs.open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESC = f.read()

setup(
    name='sura_rename',
    version='0.1.dev1',
    description='A tool to rename the Holy Quran suras',
    long_description=LONG_DESC,
    url='',
    author='Ali Salah Alddin',
    author_email='rated.ali.7@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Languae :: Python :: 3'
        ],
    keywords='quran sura',
    packages=['sura_rename'],
    install_requires=['mutagen'],
    package_data={'names': ['sura_names.json']},
    scripts=["sura-rename"]
    )
