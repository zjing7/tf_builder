"""
Tinker Free Energy Builder
Create Tinker input files for free energy simulations
"""

# Add imports here
from .mutation import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
