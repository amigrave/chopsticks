import sys

__version__ = '1.0'
__versioninfo__ = (1, 0)

DEPTH_LIMIT = getattr(sys, '_chopsticks_depthlimit', 2)

# Set `chopsticks.allow_site_imports` to True to allow the remote Python to
# import from its own site-packages. This basically removes -sS flags from the
# remote Python invocation).
#
# This option can also be set via the CHOPSTICKS_ALLOW_SITE_IMPORTS environment
# variable.
allow_site_imports = False
