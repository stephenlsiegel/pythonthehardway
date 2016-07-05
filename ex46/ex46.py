# A Project Skeleton

# This will be where you start learning how to set up a good project "skeleton" directory. When you make a new directory, just copy this directory to a new name and edit the files to get started.

# Install the following Python packages:
	# 1. pip from http://pypi.python.org/pypi/pip
		# successfully updated it on Mac with pip install -U pip
	# 2. distribute from http://pypi.python.org/pypi/distribute
		# distribute is now part of Setuptools, already installed on Mac
	# 3. nose from http://pypi.python.org/pypi/nose/
	# 4. virtualenv from http://pypi.python.org/pypi/virtualenv
		# already installed on Mac

# Creating the Skeleton Project Directory

	# We make a projects folder with skeleton folder inside of it. Inside the skeleton folder is:
	# 	bin
	# 	NAME (this will be renamed to whatever you are calling your project's main module)
	# 	tests
	# 	docs

	# We create an empty Python module directories we can put our code into. Then we need to create a setup.py file we can use to install our project later if we want:

# setup.py
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Stephen Siegel',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'stephenlsiegel@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME']
	'scripts': [],
	'name': 'projectname'
}

setup(**config)


# tests/NAME_tests.py
from nose.tools import *
import NAME

def setup():
	print "SETUP!"

def teardown():
	print "TEAR DOWN!"

def test_basic():
	print "I RAN!"

# Final Directory Structure:

# skeleton/
# 	NAME/
# 		__init__.py
# 	bin/
# 	docs/
# 	setup.py
# 	tests/
# 		NAME_tests.py
# 		__init__.py