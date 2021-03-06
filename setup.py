try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'name': 'pyJect',
	'version': '2.2.0',
	'author': 'Kyle Roux',
	'author_email': 'jstacoder@gmail.com',
	'description': 'a command line tool to make and orginize projects',
	'long_description': open('README','r').read(),
	'packages': ['pyject'],
    'py_modules': ['pyject'],
    'install_requires': ['iniparse'],
	'entry_points': {
		'console_scripts': [
			'pyject = pyject.main:main'
			]
		}
	}

setup(**config)
