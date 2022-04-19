import pytest


@pytest.mark.smoke
def test_login():
    print("Logged in success")


@pytest.mark.regression
def test_addproducts():
    print("Add products")


@pytest.mark.smoke
def test_logout():
    print("Logged out")
