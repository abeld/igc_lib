# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='igc_lib',
    version='0.1',

    packages=['igc_lib',
              'igc_lib.lib',
              ],
    install_requires=[
        'simplekml >= 1.2.2',
    ],

    author='Marcin Osowski',
    author_email='??',
    description='A simple library to parse IGC logs and extract thermals.',
    url='https://github.com/xiadz/igc_lib.git',
)
