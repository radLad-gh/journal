# Project Summary:
# command-line prompt for entering information that is appended to a day-specific .txt
# file at a designated location.
#
# requirements:
# Command-line piping (typing 'python /file/path/filename.py' can be shortened if the
# script is located in the default location for cmd)
# File conditional check and creation
# Proper appending to file with contents of STDIN

import os
import time
from datetime import datetime

# Init Input Validation
# Check/Default for Cur Folder(Designated by year and sub by month) in desigLoc
# Check for cur .txt file based on date provided by datetime
# If exists, open to append content, writing with time at head of line
# Else, create and append content, writing with time at head of line.
# Output


def getTime():
    # Time mod for head of entry
    init_time = str(datetime.now())

    slice_object_full = slice(16)
    full_datetime = init_time[slice_object_full]

    return full_datetime


def write():
    full_datetime = getTime().split(' ')
    date = full_datetime[0].split('-')

    # check exist year/month dirs, create if not exist.
    path = os.getcwd()
    target_path = f'{path}\\Journal\\{date[0]}\\{date[1]}\\'
    if not os.path.isdir(target_path):
        os.mkdir(target_path)
    else:
        pass

    keywords = input(f' Entry Keywords:\n>>')
    print(f' Date: {full_datetime[0]} Time: {full_datetime[1]}\r\n')
    content = (input(f' Tell me EVERYTHING:\n>> '))

    line_length = 70
    justified_content = [content[i:i+line_length] for i in range(0, len(content), line_length)]

    file_path = f'{path}\\Journal\\{date[0]}\\{date[1]}\\{full_datetime[0]}.txt'
    with open(file_path, 'a+') as f:
        f.write(f'{full_datetime[0]}, {full_datetime[1]}, Keywords:{[keywords]}\n')
        for line in justified_content:
            f.write(f'{line}\n')
        f.write('\r\n')


def fileScraper():
    file_list = []

    year = input(" Which YEAR would you like to search:  <FORMAT: YYYY>\n> ")
    month = input(" Which MONTH would you like to search:  <FORMAT: MM>\n> ")
    kw = input(" What word would you like to find in the records: \n> ")
    print('\r\n Thank you. One moment, please...')

    path = f'{os.getcwd()}\\Journal\\{year}\\{month}\\'

    for file in os.listdir(path):
        with open(f'{path}\\{file}') as f:
            if kw in f.read():
                file_list.append(file)

    return file_list, path


def searchUX():
    file_list, path = fileScraper()
    print(f'There were {len(file_list)} files that contained the keyword.\n')
    if len(file_list) > 0:
        for file in file_list:
            print(f'\t{file}')
        print()
        read_res = input(f'Would you like to read the files listed(Y/N)?\n> ')
        if read_res.lower() == 'y':
            for file in file_list:
                # command prompt piping to open the files with keyword matches
                os.system(f'cmd /c "{path}\\{file}"')
            search_again = input('Would you like to search again(Y/N)?\n> ')
            if search_again.lower() == 'y':
                searchUX()
            else:
                quit()
        else:
            quit()


res = int(input(' Select a number to proceed:\r\n0. New\r\n1. Search\r\n\r\n> '))
if res:
    searchUX()
else:
    write()

# This code was written by Justice Smith
# Have Fun, use it responsibly.

# To implement a search function, I can:
# Designate a target directory and then iterate through the files for keywords(1 first)
# This requires parsing the keywords list in each entry(regex?)
# Return entry path or contents?


