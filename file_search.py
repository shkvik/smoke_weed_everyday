import os

def GetDirsNames(dir):
    dirs = []
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            dirs.append(os.path.join(dir, file))
            print(os.path.join(dir, file))
    return dirs
