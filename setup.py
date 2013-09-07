# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='',
    version='',
    description='',
    long_description=readme,
    author='David Tran',
    author_email='david@crowdbooster.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

