import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Добавляет возможность передавать язык через командную строку."""
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language: --language=es or --language=fr'
    )

@pytest.fixture(scope='function')
def browser(request):
    """Фикстура инициализации браузера с нужным языком."""
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()