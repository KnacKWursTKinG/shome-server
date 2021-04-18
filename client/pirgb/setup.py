#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="pirgb",
    description="pirgb client for shomeserver plugin control (gui + cli)",

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'pirgb = pirgb._click:cli'
        ]
    },

    data_files=[
        ('share/applications', ['pirgb.desktop']),
        ('share/icons', ['pirgb.png'])
    ],

    install_requires=[
        'requests',
        'click',
        'click-aliases',
        'flask',
        'kwking_helper @ git+https://github.com/KnacKWursTKinG/helper@main'
    ],

    version="0.1.0",
    maintainer='Udo Bauer',
    maintainer_email='knackwurstking.tux@gmail.com',
    url='https://github.com/KnacKWursTKinG/shome-server',
)
