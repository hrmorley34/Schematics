from setuptools import setup
import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True
    extra['convert_2to3_doctests'] = ['README.md']

setup(
    name='schematics',
    version = '1.0',
    description='Schematic Representer',
    package_dir = {'': 'src'},
    packages = ['schematics'],
    **extra
)
