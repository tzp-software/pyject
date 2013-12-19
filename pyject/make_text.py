'''
	pyject.make_text.py
'''
import time
from data import get_username_and_email

def make_header(filename,username=None,email=None):
	txt = '''
\'\'\'
	name: {0}
	author: {1}
	email:  {2}
	date:   {3}
\'\'\'
'''
	if not filename.endswith('.py'):
		filename = filename + '.py'
	userinfo = get_username_and_email()
	if username is None:
		username = userinfo[0]
	if email is None:
		email = userinfo[1]
	date = time.ctime(time.time())
	return txt.format(filename,username,email,date)

def make_main(fileName):
    txt = '''

def {0}():
    pass

def test():
    pass

def main():
    {0}()

if __name__ == "__main__":
    main()
    '''.format(fileName)
    hdr = make_header(fileName)
    return hdr + '\n' + txt

def make_nosetest(fileName):
	hdr = make_header(fileName)
	txt = '''
import nose.tools as nt
import nose

def setup():
	pass

def teardown():
	pass

if __name__ == "__main__":
	nose.main()
'''
	return hdr + txt

def make_test(fileName):
	return make_nosetest(fileName)

def make_unittest(fileName):
    txt = '''

import unittest

class Test{0}(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_{}(self):
        assertTrue(True)

if __name__ == "__main__":
    unittest.main()

    '''.format(fileName)
    return txt

def make_setup(name):
    txt = '''
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': ,
    'version': '0.0.1',
    'author': 'Kyle Roux',
    'author_email': 'jstacoder@gmail.com',
    'description': '',
    'long_description': open('README','r').read(),
    'py_packages':
    }
setup(**config)
    '''
    return txt
