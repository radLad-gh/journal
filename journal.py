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
from datetime import datetime

# Init Input Validation
# Check/Default for Cur Folder(Designated by year and sub by month) in desigLoc
# Check for cur .txt file based on date provided by datetime
# If exists, open to append content, writing with time at head of line
# Else, create and append content, writing with time at head of line.
# Output

path = os.getcwd()

# Time mod for head of entry
initTime = str(datetime.now())

slice_object_full = slice(16)
slice_object_date = slice(10)
slice_object_year = slice(4)
slice_object_month = slice(5, 7)

full_datetime = initTime[slice_object_full]
date = initTime[slice_object_date]
year = initTime[slice_object_year]
month = initTime[slice_object_month]
print(f'Datetime: {full_datetime}\r\n')

# check exist year/month dirs, create if not exist.
if not os.path.isdir(f'{path}\\Journal'):
    os.mkdir(f'{path}\\Journal\\')
    if not os.path.isdir(f'{path}\\Journal\\{month}\\'):
        os.mkdir(f'{path}\\Journal\\{month}\\')
    else:
        pass
else:
    pass

# Generator if want to change the list comprehension method
# def linesplit(s, n):
#     for start in range(0, len(s), n):
#         yield s[start:start+n]


content = (input(f'Tell me EVERYTHING:\n>> '))
lineLength = 70
justifiedContent = [content[i:i+lineLength] for i in range(0, len(content), lineLength)]

filepath = f'{path}\\Journal\\{month}\\{date}.txt'
with open(filepath, 'a+') as f:
    f.write(f'{full_datetime}\n')
    for line in justifiedContent:
        f.write(f'{line}\n')
    f.write('\r\n')

# This code was written by Justice Smith
# Have Fun, use it responsibly.






