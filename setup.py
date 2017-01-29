#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os.path import abspath, dirname, join as pjoin
from os import chdir, environ
import pip
import io
import codecs
import os
import sys
import DiscoNet


environ['USE_OSX_FRAMEWORKS'] = '0'
if environ.get('READTHEDOCS', None) == 'True':
    # Temporarily grab known working Kivy for readthedocs.org from git
    #future environ['KIVY_GL_BACKEND'] = 'mock'
    environ['USE_OPENGL_MOCK'] = '1'
    pip.main(['install', 'https://github.com/kivy/kivy/archive/2d5b365747284b029c8a2b3291ca0f4d580e7b86.zip'])

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


if len(sys.argv) > 1 and ('install' in sys.argv[1] or 'develop' in sys.argv[1]):
    
    
    if len(sys.argv) < 3 or ('-u' not in sys.argv[2] and '--uninstall' not in sys.argv[2]):
        with io.open('requirements.txt') as reqs:
            for req in reqs:
                pip.main(['install', req])


long_description = read('README.rst')

setup(
    name=DiscoNet.__name__,
    version=DiscoNet.__version__,
    url=DiscoNet.__url__,
    packages=find_packages(),
    install_requires=['docutils>=0.3',
                      'kivy.deps.sdl2>=0.1.12; sys_platform == "win32"',
                      'kivy.deps.glew>=0.1.4; sys_platform == "win32"',
                      'kivy>=1.9.0',
                      'openpyxl>=2.4.1',
                      'paramiko>=2.1.1',
                      'pypiwin32>=219; sys_platform == "win32"',
                      'winshell>=0.6; sys_platform == "win32"',
                    ],
    package_data={
        '': ['*.kv', '*.ico', '*.png', '*.icns'],
    },
    author=DiscoNet.__author__,
    author_email=DiscoNet.__email__,
    description=DiscoNet.__description__,
    long_description=long_description,
    license=DiscoNet.__license__,
    keywords='net network discovery excel xlsx scan scanner tool subnet ip',
    entry_points={
        'console_scripts': ['discoveryscan = DiscoNet.discoveryscan:_main',],
        'gui_scripts': ['DiscoNet = DiscoNet.__main__:run',],
        },
)

