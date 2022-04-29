import os
import shutil
import glob
from datetime import datetime

print(os.getcwd())
if os.path.exists("textfiles"):
    print("yes, exists")
else:
    print("no existance")
    os.makedirs("textfiles")
    #could use this to set up everyones computer
print(os.getcwd())

files = glob.glob("*.txt")
print(files)

for file in files:
    print(file)
    shutil.copy(file, "textfiles") #copies file to new folder