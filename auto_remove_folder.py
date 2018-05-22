ip'''
DESC: This script will removed Solved folders from a directory
UNLESS the parent folder contains -Ins_ in it
CAUTION: folder needs to be changed to current user's path
Potentially moving the files to the folder could be automated as well
AUTHOR: Patty Jula
DATE: May 2018
'''

# import modules
import os
import os.path
import shutil

# folder needs to be changed
folder = 'C:/Users/username/Activities'
dirs = [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder,d))]

for dir in dirs:
    # skip folders containing -Community_
    if '-Community_' not in dir:
        val = os.path.join(folder, dir)
        print(val)
        subdirs = [
                   d for d in os.listdir(os.path.join(folder, dir))
                   if os.path.isdir(os.path.join(folder, dir))
                  ]
        for subdir in subdirs:
            if subdir == "Solved":
                # Join with parent directory
                solved_folder = os.path.join(val, subdir)
                print(solved_folder)
                # Remov folder
                shutil.rmtree(solved_folder)
            else:
                continue
    else:
        continue
