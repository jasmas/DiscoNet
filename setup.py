#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from os.path import abspath, dirname, join as pjoin
from os import chdir, environ
import io
import codecs
from setuptools import setup, find_packages
import DiscoNet


environ['USE_OSX_FRAMEWORKS'] = '0'
if environ.get('READTHEDOCS', None) == 'True':
    import pip
    pip.main(['install', 'https://github.com/kivy/kivy/archive/master.zip'])

here = abspath(dirname(__file__))
chdir(here)

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

setup(
    name=DiscoNet.__name__,
    version=DiscoNet.__version__,
    url=DiscoNet.__url__,
    packages=find_packages(),
    install_requires=['docutils>=0.3',
                      'future>=0.16.0',
                      'openpyxl>=2.4.1',
                      'paramiko>=2.1.1',
                      ],
    extras_require={
        ':sys_platform == "win32"': [
            'pypiwin32>=219',
            'winshell>=0.6',],
        'GUI': [
            'kivy.deps.sdl2>=0.1.12; sys_platform == "win32"',
            'kivy.deps.glew>=0.1.4; sys_platform == "win32"',
            'Kivy>=1.9.0',],
        },
    package_data={
        '': ['*.kv', '*.ico', '*.png', '*.icns'],
    },
    author=DiscoNet.__author__,
    author_email=DiscoNet.__email__,
    description=DiscoNet.__description__,
    long_description=DiscoNet.__doc__,
    license=DiscoNet.__license__,
    keywords='net network discovery excel xlsx scan scanner tool subnet ip',
    entry_points={
        'console_scripts': ['discoveryscan = DiscoNet.discoveryscan:_main',],
        'gui_scripts': ['DiscoNet = DiscoNet.__main__:run [GUI]',],
        },
)

