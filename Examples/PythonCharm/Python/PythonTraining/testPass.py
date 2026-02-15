
import pytest

def resource_1_setup():
    print('into Setup')

def resource_1_teardown():
    print('into Teardown')

# def setup_module(module):
#     print('\nSetup of module is called')
#     resource_1_setup()
#
# def teardown_module(module):
#     print('\nTeardown of module is called')
#     resource_1_teardown()

def test_1_using_resource_1():
    print('noPom 1')

def test_2_using_resource_1():
    print('noPom 2')

    print ('hello Wolrd')



