
import os
import sys

module_path = os.path.abspath(__file__).rsplit('/', 2)[0]
sys.path.insert(0, module_path)

from pirgb._click import cli

cli()
