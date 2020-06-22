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

    keywords = input(f'Entry Keywords:\n>>')
    print(f'Date: {full_datetime[0]} Time: {full_datetime[1]}\r\n')
    content = (input(f'Tell me EVERYTHING:\n>> '))

    line_length = 70
    justified_content = [content[i:i+line_length] for i in range(0, len(content), line_length)]

    file_path = f'{path}\\Journal\\{date[0]}\\{date[1]}\\{full_datetime[0]}.txt'
    with open(file_path, 'a+') as f:
        f.write(f'{full_datetime[0]}, {full_datetime[1]}, Keywords:{[keywords]}\n')
        for line in justified_content:
            f.write(f'{line}\n')
        f.write('\r\n')


def search():
    kw = input("What word would you like to find in the records: ")
    print('\r\nThank you. One moment, please...')
    time.sleep(1)


res = int(input('Select a number to proceed:\r\n0. New\r\n1. Search\r\n\r\n>> '))
if res:
    print('This function is currently under servicing and will be available soon. \r\nThank you for your support.')
    quit()
else:
    write()

# This code was written by Justice Smith
# Have Fun, use it responsibly.

