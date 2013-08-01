'''
	pyject.main.py

	command line tool for pyject
'''
from data import list_all, print_usage
from make_dir import add_package
from projects import create_project
from make_file import add_module
import sys

def main():
	if len(sys.argv) > 1:
		args = sys.argv[1:]
		if args[0] == '-c' or args[0] == '--create-project':
			create_project(args[1])
		elif args[0] == '-m' or args[0] == '--add-module':
			add_module(args[1],args[2])
		elif args[0] == '-p' or args[0] == '--add-package':
			add_package(args[1],args[2])
		elif args[0] == '-l' or args[0] == '--list-all':
			list_all()
		elif args[0] == '-h' or args[0] == '--help':
			print_usage
		else:
			print 'Error: Command Line Option Not Recognized'
			sys.exit(1)
	else:
		print_usage()




