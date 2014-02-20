#!/usr/bin/env
# -*- coding: utf-8 -*-

from setuptools import setup


def read(fname):
    # makes sure that setup can be executed from a different location
    import os.path
    _here = os.path.abspath(os.path.dirname(__file__))
    return open(os.path.join(_here, fname)).read()

setup(
    name='testserver',
    version='0.01-b0002',
    author='Bastrykov Evgeniy',
    author_email='vporoshok@gmail.com',
    license='MIT License',
    description='''Threaded daemon localhost http server. Simple HEAD, GET,
                PUT and POST request parsing for unittest.''',
    long_description=read('README.md'),
    url='https://github.com/vporoshok/testserver',
    download_url='https://github.com/vporoshok/testserver/releases',
    zip_safe=False,
    include_package_data=True,
    keywords='unittest server localhost http REST',
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Testing'
    ]
)
