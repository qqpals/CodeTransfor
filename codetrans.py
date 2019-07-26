#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jerry'

'''please run this script with sudo right'''

import os
import sys


def getfile(file_dir):
    filesList = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.srt':
                #L.append(os.path.join(root, file))
                filesList.append(file)
    return filesList

def code_chage(files_list):
    for filename in files_list:
        os.system( 'dos2unix "{}" >/dev/null 2>&1'.format(filename))
        portion = os.path.splitext(filename)
        os.system('iconv -f "gbk" -t "utf-8" "{}" > "{}"'.format(filename, portion[0] + '-1' + '.srt'))
    return

def main():
    files_list = getfile('.')
    code_chage(files_list)

if __name__ == '__main__':
    main()