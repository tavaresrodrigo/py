import os
pwd = os.getcwd()
pwdVideos = os.path.join(pwd, 'videos')
pwdMusic = os.path.join(pwd, 'music')
pwdImages = os.path.join(pwd, 'images')
folders = ['images','music','videos']

# Creating the folders
try:
    for folder in folders:
        os.mkdir(os.path.join(pwd, folder))
except FileExistsError: 
    print ('Folders %s already created' %folders)
except OSError:
    print ('Creation of the directory %s failed' % folders)
else:
    print ('Successfully created the direcotires %s' %folders)

# Identifying the files and moving to their respective folders
for file in os.listdir(pwd):
    if file.endswith(".mov") or file.endswith(".avi"):
        os.rename(os.path.join(pwd,file), os.path.join(pwdVideos, file))
    elif file.endswith(".mp3") or file.endswith(".flac"):
         os.rename(os.path.join(pwd,file), os.path.join(pwdMusic, file))
    elif file.endswith(".jpg") or file.endswith(".png"):
         os.rename(os.path.join(pwd,file), os.path.join(pwdImages, file))
    elif file.endswith(".log"):
        os.remove(file)
