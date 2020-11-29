import os, sys
files = os.listdir(os.getcwd())
files.sort()
fileDic = {}
for file in files:
    fileDic.update({file:os.stat(file).st_size})

sortedFileDic = sorted(fileDic.items(), key=lambda x: x[1], reverse=True)
print (sortedFileDic)

for i in sortedFileDic:
    print (i[0], i[1])