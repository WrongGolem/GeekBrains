import os
import shutil

directory = os.path.join(os.path.dirname(__file__), 'my_project1')
folder=os.path.join(os.path.dirname(__file__), 'my_project1', 'templates')

if not os.path.exists(folder):
    os.makedirs(folder)

for root, dirs, files in os.walk(directory):
    if root.count('templates'):
        for dir_ in dirs:
            if not os.path.exists(os.path.join(folder, dir_)):
                os.makedirs(os.path.join(folder, dir_))
        for file in files:
            file_1 = os.path.join(root, file)
            file_2 = os.path.join(folder, os.path.basename(root))
            if not os.path.dirname(file_1) == file_2:
                shutil.copy(file_1, file_2)

