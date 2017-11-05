#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='brutalmaze',
    version='0.0.3',
    description='A research hash and slash game with fast-paced action and a minimalist art style',
    long_description=long_description,
    url='https://github.com/McSinyx/brutalmaze',
    author='Nguyễn Gia Phong',
    author_email='vn.mcsinyx@gmail.com',
    license='GPLv3+',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Games/Entertainment :: Arcade'],
    keywords='pygame action-game',
    packages=['brutalmaze'],
    install_requires=['pygame>=1.9'],
    package_data={'brutalmaze': ['icon.png']},
    entry_points={'gui_scripts': ['brutalmaze = brutalmaze:main']})
