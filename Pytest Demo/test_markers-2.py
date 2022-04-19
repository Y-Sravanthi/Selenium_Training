import sys

import pytest
import sys

@pytest.mark.skip
def test_login():
    print("Logged in success")

@pytest.mark.skipif(sys.version_info>(3,9),reason="Python version is not supported")
def test_addproducts():
    print("Add products")

def test_logout():
    print("Logged out")