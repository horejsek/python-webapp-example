#!/usr/bin/env python3

import setuptools


with open('README.md') as f:
    long_description = ''.join(f.readlines())


setuptools.setup(
    name='webapp',
    version='1.0',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,

    description='Example of Python web app with debian packaging (dh_virtualenv & systemd)',
    long_description=long_description,
    author='Michal Horejsek',
    author_email='horejsekmichal@gmail.com',
    url='https://github.com/horejsek/python-webapp',

    # All versions are fixed just for case. Once in while try to check for new versions.
    install_requires=[
        'flask==1.0.2',
        'psycopg2==2.7.5',
    ],

    # Do not use test_require or build_require, because then it's not installed and
    # can be used only by setup.py. We want to use it manually as well.
    # Actually it could be in file like dev-requirements.txt but it's good to have
    # all dependencies close each other.
    extras_require={
        'devel': [
            'mypy==0.620',
            'pylint==2.1.1',
            'pytest==3.7.1',
        ],
    },

    entry_points={
        'console_scripts': [
            'webapp = webapp.cli:main',
        ],
    },

    classifiers=[
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    zip_safe=False,
)
