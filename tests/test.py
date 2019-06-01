# =============== Imports =============== #
import sys
import os

from protecc import protecc

# =============== Setup =============== #
sys.path.append(os.path.abspath('../protecc'))

# =============== Main =============== #
def test():
    assert protecc is not None
