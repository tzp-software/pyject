'''
	pyject.data.py
'''
import sys

USER = 'Kyle Roux'
EMAIL = 'jstacoder@gmail.com'

def list_all():
	print 'listing all packages'
	from root import ROOT_DIR
	import os
	print 'Projects in root dir:'
	for itm in os.listdir(ROOT_DIR):
		print itm

def print_usage():
	usage = '''
USAGE: pyject [-c PROJECT] [-m PROJECT [PACKAGE] MODULE] [-p PROJECT PACKAGE] 
[-w PROJECT [PACKAGE]] [-l]
	
Options:
-c, --create-project PROJECT                make a new project named PROJECT
-m, --add-module PROJECT [PACKAGE] MODULE   make a new module MODULE in PROJECT/PACKAGE
-p, --add-package PROJECT PACKAGE           make new package PACKAGE in PROJECT
-w, --work PROJECT [PACKAGE]                cd to PROJECT or PACKAGE dir to work on files
-l, --list-all                              list all projects in main root dir

Tzp-Software		kyle roux

	'''
	print usage
	sys.exit(1)

