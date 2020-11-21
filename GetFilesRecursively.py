import glob, os
from num2words import num2words 
from pathlib import Path
from os import path

pwd = os.getcwd()
wordToSearch = 'two'
txtFolder = os.path.join(pwd, 'txtfolder')

## Creating the folder for testing
try:
    os.mkdir(txtFolder)
except FileExistsError: 
    print ('Folders %s already created' %txtFolder)

# Creating the files to test the recursive search
for i in range(10):
    fileName = os.path.join(txtFolder, str(i)+'.txt')
    if path.exists(fileName) == True:
        print (fileName + ' already created in '+ txtFolder)
    else:
        txFfile = open(fileName, 'w')
        txFfile.write(num2words(i))
        txFfile.close()

# Getting all the occurrences of a word within *.txt files
def get_occurrences (filename,word):
    file = open(filename)
    StringFile = file.read()
    n = StringFile.count(word)
    if n > 0:
        occurrences = n
        print(str(filename) +' has '+ str(occurrences)+' of the world ' + word)

# Getting the files in the folder per extention  
for file in glob.glob('*.txt'):
    print(file)
    get_occurrences(file,wordToSearch)

for file in Path(pwd).rglob('*.txt'):
    print(file)
    get_occurrences(file,wordToSearch)
