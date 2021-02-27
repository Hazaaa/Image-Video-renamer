# importing os module 
import os 
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory
from alive_progress import alive_bar
  
# Function to rename multiple files 
def main(): 
  
    # shows dialog box and return the path of source and destination folder
    sourceFolderPath = askdirectory(title='Select Source Folder')
    destinationFolderPath = askdirectory(title='Select Destination Folder')

    # get all files from source folder
    allFiles = os.listdir(sourceFolderPath)

    # define progress bar
    with alive_bar(len(allFiles), title='Renaming...') as bar:
        for file in allFiles: 
            name, extension = file.split('.')
            
            splittedName = name.split('_')
            splittedNameCount = len(splittedName)

            correctName = ""

            # checking if image/video has prefix (eg. IMG, VID, PIX, ...)
            if splittedNameCount == 3:
                splittedName.pop(0)
                correctName = '_'.join(splittedName) + '.' + extension
            elif splittedNameCount == 2:
                correctName = file
            else:
                # this is for invalid files
                correctName = ""

            fileSource = sourceFolderPath + '/' + file
            fileDestination = destinationFolderPath + '/'

            if correctName != "":
                fileDestination = fileDestination + correctName
            else:
                # all invalid files are copied in invalidFiles folder
                invalidFilesPath = fileDestination + 'invalidFiles'
                if not os.path.exists(invalidFilesPath):
                    os.mkdir(fileDestination + 'invalidFiles')

                fileDestination = invalidFilesPath + '/' + file

            # if file is already renamed skip copying (for eg. if app is started twice)
            if not os.path.exists(fileDestination):
                # copy2 is saving all metadata
                shutil.copy2(fileSource, fileDestination)
            else:
                bar.text("Copying file skipped: File already renamed")
            
            # update progress bar
            bar()
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()