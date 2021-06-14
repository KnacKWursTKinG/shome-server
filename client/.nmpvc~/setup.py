#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="nmpv_client",
    description="control nmpv shomeserver plugin",

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'nmpvc = nmpvc._click.nmpv:cli'
        ]
    },

    #data_files=[
    #    ('share/applications', ['pirgb.desktop']),
    #    ('share/icons', ['pirgb.png'])
    #],

    install_requires=[
        'requests',
        'dill',
        'pysmb',
        'click',
        'click-aliases',
        'flask',
        'kwking_helper @ git+https://github.com/KnacKWursTKinG/helper@main'
    ],

    version="0.0.1",
    maintainer='Udo Bauer',
    maintainer_email='knackwurstking.tux@gmail.com',
    url='https://github.com/KnacKWursTKinG/shome-server',
)
