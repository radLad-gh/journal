## Journal
This is a Python Journal Script for Windows to append information to a DirTree.

# IMPORTANT!
The python script was written and tested on a Windows 10 system and no other. \
Additionally, because the script checks for cwd at init, it is recommended that \
you call the file from the default location of command prompt. 

## Project Summary:
 command-line prompt for entering information that is appended to a day-specific .txt\
 file at a designated location.
 
## Functions:
Write():\
 Allows you to create an entry that is filed by date in the appropriate directory branch.

Search():
 Allows you to search files within a specified month for a chosen keyword. It then \
 returns a list of the files that contain the keyword as well as the option to open them \
 sequentially, after which the program terminates. 

## Looking Ahead:
The search function currently has no implementation and simply returns a makeshift \
'Out of Order' message. 

I plan to have it:
1. Search by:\
   [year, month, day(of the month or week), time span(between a and b)]
2. Filter by:\
   [date, time of day, other words in text]
   
~~I have no knowledge of how to search through files but plan to learn and implement \
at least a basic functionality on or before 6.25.2020 to allow for at minimum a single \
keyword search.~~

## Milestones: 
6.25.2020: Added search function that allows for single keyword lookups. 


