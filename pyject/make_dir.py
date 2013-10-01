'''
	pyject.make_dir.py
'''
from root import get_env_root
import os


def add_package(projectName,packageName):
	#print 'Adding package {} to project {}'.format(packageName,projectName)
    ROOT_DIR = get_env_root()
    if not os.path.exists(ROOT_DIR):
        os.makedirs(ROOT_DIR)
    os.chdir(ROOT_DIR)

    if not projectName in os.listdir(ROOT_DIR):
        print '{} does not exist!'.format(projectName)
    if os.path.exists(os.curdir + os.sep + projectName + os.sep + packageName):
        print '{} exists! cannot overwrite with pyject! must do it by hand!'.format(packageName)
    dir = projectName + os.sep + projectName + os.sep + packageName
    
    if os.makedirs(dir):
        print 'Made {}'.format(dir)
    else:
        print 'Error making {}'.format(dir)
