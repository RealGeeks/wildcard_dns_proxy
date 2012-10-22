#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

setup(
    name='wildcard_dns_proxy',
    version='0.0.1',
    description='A proxying DNS server that supports wildcards',
    author='Kevin McCarthy',
    author_email='me@kevinmccarthy.org',
    url='https://github.com/realgeeks/wildcard_dns_proxy',
    packages=find_packages(),
    license='BSD',
    entry_points={
        'console_scripts': [
            'wildcard_dns_proxy = dnsproxy.main:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: System :: Installation/Setup',
        'Topic :: Software Development :: Version Control',
        'License :: OSI Approved :: MIT License',
    ],
)
