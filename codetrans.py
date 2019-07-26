#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jerry'

'''please run this script with sudo right'''

import os
import sys

'''
def getfile(file_dir):
    filesList = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.srt':
                #L.append(os.path.join(root, file))
                filesList.append(file)
    return filesList
'''
def code_chage(filename):

    os.system( "dos2unix {}".format(filename))
    portion = os.path.splitext(filename)
    str = "iconv -f 'gbk' -t 'utf-8' {} > {}".format(filename, portion[0] + '-1' + '.srt')
    os.system(str)
    #ps = subprocess.Popen(str)
    #ps.wait()


    return

def main():
    #files_list = getfile('.')

    if(len(sys.argv) != 2):
        print("please input filename!")
    else:
        code_chage(sys.argv[1])

if __name__ == '__main__':
    main()