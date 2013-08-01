'''
	pyject.data.py
'''
import sys

USER = 'Kyle Roux'
EMAIL = 'jstacoder@gmail.com'

def list_all():
	print 'listing all packages'

def print_usage():
	usage = 'USAGE: pyject [-c ProjectName] [-m ProjectName ModuleName] [-p ProjectName PackageName] [-l]'
	print usage
	sys.exit(1)

