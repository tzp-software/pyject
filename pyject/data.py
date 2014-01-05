'''
	pyject.data.py
'''
import os
import sys
from iniparse import INIConfig


USER = 'Kyle Roux'
EMAIL = 'jstacoder@gmail.com'

def make_cfg():
    parser = INIConfig()
    name = raw_input('Please enter your username: ')
    parser.userinfo.username = name
    email = raw_input('please enter your email: ')
    parser.userinfo.email = email
    cfg = '.pyject.cfg'
    cfgpath = os.path.join(os.path.expanduser('~'),cfg)
    f = open(cfgpath,'w')
    f.write(str(parser)+'\n')
    f.close()

def list_all():
    print 'listing all packages'
    from root import ROOT_DIR
    import os
    if not os.path.exists(ROOT_DIR):
        os.makedirs(ROOT_DIR)
    print 'checking projects in root dir....'
    itms = os.listdir(ROOT_DIR)
    if itms:
        print 'Projects:'
        print '\n'.join(map(str,itms))
    else:
        print 'No projects found'

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

def get_username_and_email(name=None,email=None):
    cfg = '.pyject.cfg'
    cfgpath = os.path.join(os.path.expanduser('~'),cfg)
    if not os.path.exists(cfgpath):
        make_cfg()
	ini = INIConfig(file(cfgpath))
	if name is None:
		name = ini.userinfo.username
	if email is None:
		email = ini.userinfo.email
	return (name,email)
