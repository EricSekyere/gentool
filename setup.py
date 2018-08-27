#!/usr/bin/env python
from setuptools import setup, find_packages

LONG_DESCRIPTION = """
gtools is a simple python general tool cli to interact with the file systems
in windows/linux

The tool can perform operations like unnziping files in folders recursively
""".strip()

SHORT_DESCRIPTION = """
A simple  cli for interacting with the file system.
"""

VERSION = "1.0.0"

URL = "https://ericsekyere.ca"

DEPENDENCIES = ['Click']

setup(
    name='gtools',
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    author='Eric Sekyere',
    author_email='ericsekyere1@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=DEPENDENCIES,
    keywords='command line interface cli python filesystem ',
    entry_points={
        'console_scripts': ['gtools=cli:gtools']
    },
)