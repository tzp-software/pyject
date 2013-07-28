try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'name': {},
	'version': {},
	'author' : {},
	'author_email': {},
	'description': '',
	'long_description': open('README','r').read(),
	}

setup(**config)
