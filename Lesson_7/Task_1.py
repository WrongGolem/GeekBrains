import os

dir_name = 'my_project'
folders = ('settings', 'mainapp', 'adminapp', 'authapp')

if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    for folder in folders:
        dir_path = os.path.join('my_project', folder)
        os.makedirs(dir_path)
