from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    print("\n Initialize browser session")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\n Finish browser session")
    browser.quit()