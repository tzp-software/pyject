'''
    pyject.tests.main_tests.py
'''
from nose.tools import *

def setup():
    print 'Setting up'

def teardown():
    print 'killing test vars'

def test_test():
    print 'Running a gay test'
    for x in range(10):
            print 'test '+str(x)


