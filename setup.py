#!/usr/bin/env python3

from setuptools import setup

with open('requirements.txt', 'r') as f:
	required = f.read().splitlines()

setup(
	name="pyprof",
	version='1.0',
	author="Aditya Agrawal",
	author_email="aditya.iitb@gmail.com",
	maintainer="Aditya Agrawal",
	maintainer_email="aditya.iitb@gmail.com",
	url="https://github.com/adityaiitb/pyprof",
	license="BSD 3-Clause License",
	packages=['pyprof', 'pyprof.nvtx'],
	install_requires=required,
)
