'''
	pyject.projects.py
'''
from root import go_to_root
import sys
import os

def create_project(projectName):
	go_to_root()
	print 'Creating a new project named {}'.format(projectName)
	if os.path.exists(projectName):
		print 'Error: {} project dir already exists'.format(projectName)
		sys.exit(1)
	else:
		os.mkdir(projectName)



