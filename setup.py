# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='autonoom',
    version='0.0.1',
    description='Autonomous car software',
    long_description=readme,
    author='InHolland',
    author_email='',
    url='https://github.com/autonoom/autonoom',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

