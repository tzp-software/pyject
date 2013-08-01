import os
import sys

ROOT_DIR = os.path.expanduser('~')  + os.sep + '.pyject_projects'

def check_root():
	if not os.path.exists(ROOT_DIR):
		os.makedirs(ROOT_DIR)

def go_to_root():
	check_root()
	os.chdir(ROOT_DIR)

