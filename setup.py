#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="shomeserver",
    description="flask server wich will load plugins (blueprints) for doing stuff.",

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
        'flask',
        'click'
    ],

    version="0.1.0",
    maintainer='Udo Bauer',
    maintainer_email='knackwurstking.tux@gmail.com',
    url='https://github.com/KnacKWursTKinG/shome-server',
)
