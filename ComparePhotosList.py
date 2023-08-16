# ----------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------
import os
import shutil
import pandas as pd

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------

def GetFilesInDirectory(path):
    fileNamesList = []
    counter = 0
    for foldername, subfolders, filenames in os.walk(path):
        total = len(filenames)
        if foldername == path + "\.tmp.driveupload":
            continue
        for filename in filenames:
            fileNamesList.append(filename)
            counter = counter + 1
            #print(str(foldername) + " / " + str(counter) + " / " + str(total))
    return fileNamesList


# ----------------------------------------------------------------------
# Variables
# ----------------------------------------------------------------------

path = 'F:\Google_Drive'
missingFilesPath = 'F:\Google_Drive_Upload'

# ----------------------------------------------------------------------
# Main Control
# ----------------------------------------------------------------------

# Get list of files in the current folder
fileNamesList = GetFilesInDirectory(path)

# Get list of files from Google Photos
data = pd.read_csv(r'out.csv')   
df = pd.DataFrame(data, columns=['filename'])

# Get list of files in the current folder that aren't already in Google Photos
missedPhotosCounter = 0
for fileName in fileNamesList:
    if fileName not in df['filename'].values:
        missedPhotosCounter = missedPhotosCounter + 1
        print(str(missedPhotosCounter) + ": " + fileName)
        shutil.copy(os.path.join(path, fileName), missingFilesPath)
