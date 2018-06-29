import glob
import shutil

filepath = glob.glob(r"/Applications/League of Legends.app/Contents/LoL/Logs/*")

for directory in filepath:
    shutil.rmtree(directory)
