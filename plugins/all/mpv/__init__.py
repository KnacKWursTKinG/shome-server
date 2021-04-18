""" simple mpv plugin to access 'jaseg/python-mpv' from the network

Github: 'https://github.com/jaseg/python-mpv'
"""

from kwking_helper import c

if 'plugin@mpv' not in c.main.sections():
    # load default/fallback config
    c.read(__file__.rsplit('/', 1)[0] + '/config.ini')

from .route import api_blueprint

__all__ = ['api_blueprint']
