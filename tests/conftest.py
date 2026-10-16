import pytest

@pytest.fixture
def page(page):
    page.goto('https://testautomationpractice.blogspot.com/')
    return page
