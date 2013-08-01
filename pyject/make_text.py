'''
	pyject.make_text.py
'''
from data import USER, EMAIL

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
	return txt

def make_test(fileName):
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
		'name': {0},
		'version': '0.0.1',
		'author': {1},
		'author_email': {2},
		'description': '',
		'long_description': open('README','r').read(),
		'py_packages': {0}
		}

	setup(**config)
	'''.format(name,USER,EMAIL)
	return txt
