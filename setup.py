#!/usr/bin/env
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='testserver',
    version='0.02-b0003',
    author='Bastrykov Evgeniy',
    author_email='vporoshok@gmail.com',
    license='MIT License',
    description='''Threaded daemon localhost http server. Simple HEAD, GET,
                PUT and POST request parsing for unittest.''',
    url='https://github.com/vporoshok/testserver',
    download_url='https://github.com/vporoshok/testserver/releases',
    packages=[
        'testserver'
    ],
    install_requires=[
    ],
    tests_require=[
        'httplib2'
    ],
    test_suite='tests',
    zip_safe=False,
    include_package_data=True,
    keywords='unittest server localhost http REST',
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing'
    ]
)
