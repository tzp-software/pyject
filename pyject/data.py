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
	usage = 'USAGE: pyject [-c ProjectName] [-m ProjectName ModuleName] [-p ProjectName PackageName] [-l]'
	print usage
	sys.exit(1)

