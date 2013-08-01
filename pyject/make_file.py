'''
	pyject.make_file.py
'''
import os
import sys
from make_text import make_main, make_test, make_setup
from projects import create_project
from root import go_to_root

types = {
	'main': make_main,
	'test': make_test,
	'setup': make_setup,
	}

def add_module(projectName,moduleName):
	print 'adding module named {} to project {}'.format(moduleName,projectName)
	oldDir = os.getcwd()
	go_to_root()
	if not os.path.exists(projectName):
		print 'Error: {} project dir does not exist\nCreate? (y or n): '.format(projectName)
		if raw_input().lower().startswith('y'):
			create_project(projectName)
		else:
			sys.exit(1)
	
	os.chdir(projectName)
	make_main(moduleName)

	if os.path.exists(moduleName):
		print 'made python module {}'.format(moduleName)
		os.chdir(oldDir)
	else:
		sys.exit(1)
	
def make_file(fileName, txt=None):
	if os.path.exists(fileName):
		print 'Error: {} already exists!'.format(fileName)
		sys.exit(1)
	else:
		try:
			f = open(fileName,'w')
			if txt is not None:
				f.write(txt)
		except Exception:
			print 'File Error!'
		finally:
			f.close()

def get_text(name, fileType):
	return types[fileType](name)

def make_setup(projName):
	make_file(projName,get_text(projName,'setup'))

def make_main(projName):
	make_file(projName,get_text(projName,'main'))

def make_test(projName):
	make_file(projName,get_text(projName,'test'))

def make_init():
	make_file('__init__.py')

def make_manifest():
	make_file('MANIFEST.in')

def make_readme(txt=None):
	make_file('README',txt)


