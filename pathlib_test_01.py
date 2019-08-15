"""
pathlib_test_01.py
Test of pathlib modules: Comparing results of the same code for Linux and Windows
Uwe Schweinsberg 15.8.19
"""
from pathlib import Path
import os
import sys

# list directory tree structure
def list_files(startpath, txt_f):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        txt_f.write('{}{}/\n'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            txt_f.write('{}{}/\n'.format(subindent, f))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        folder = sys.argv[1:]
        if len(sys.argv) > 2:
            text_file = sys.argv[2:][0]
        else:
            text_file = 'tree + folder[0]'
        try:
            f_text = open(text_file, 'w')
        except IOError:
            print('{} could not be opend for write'.format(t_text))
            raise IOError
    else:
        raise NameError ("No command line argument (name of path) is given. ")

    f_text.write('This tree has been created with {} \n\n'.format(__file__))
    list_files(folder[0], f_text)
    f_text.close()

# get the name of the drive of the current working directory
folder = os.getcwd()