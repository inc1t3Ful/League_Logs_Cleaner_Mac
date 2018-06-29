import glob
import shutil

dirs = glob.glob(r"/Applications/League of Legends.app/Contents/LoL/Logs/*")

for directory in dirs:
    shutil.rmtree(directory)
