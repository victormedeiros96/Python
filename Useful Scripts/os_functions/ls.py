import os
def ls(path):
    files_and_folders = os.listdir(path)
    return files_and_folders

if __name__=='__main__':
    print(ls('.'))