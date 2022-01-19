import os


## print the current dir
print(os.getcwd())


## list the files in the dir
files = os.listdir(os.getcwd())
print(files)

## create the dir
#os.mkdir("Pictures") # only create a layer
os.makedirs("Pictures/trips_pictures/", exist_ok =True)
os.removedirs("Pictures/trips_pictures/")


# Remove a whole directory structure (subdirs and files)
# Like rm -rf
#shutil.rmtree(path_to_dir)

## create an single folder and remove a single folder
path = 'test'
os.mkdir(path)


files = os.listdir(os.getcwd())
print(files)
os.rmdir(path)
files = os.listdir(os.getcwd())
print(files)

## join the path and file
cur_dir = os.getcwd()
file1 = 'main.py'
combined = os.path.join(cur_dir,file1)

## check if the path exist
print(os.path.exists(combined))
print(os.path.isfile(combined))
print(os.path.isdir(combined))
print(os.stat(combined).st_size) ## file size with byte unit

##
v1 = os.environ.get("PATH")
print(v1)
print(os.getlogin())
