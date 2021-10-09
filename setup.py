#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages

setup(name='fitness_forum_master',
      version='1.0',
      description='A simple forum application with a theme of health and fitness',
      author='Shehan Atukorala',
      author_email='shehanatuk@gmail.com',
      url='',
      packages=find_packages(include=['fitness_forum.*']),
)