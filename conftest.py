import pytest
from selenium import webdriver

# Добавляем аргументы командной строки
def pytest_addoption(parser):
    # При помощи "parser.addoption" добавляем аргументы для выбора
    # браузера и для выбора языка
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en-gb',
                     help='Choose the language for page')

@pytest.fixture
def browser(request):
    # Берем имя браузера из командной строки browser_name и
    # присваем его "browser name"
    browser_name = request.config.getoption('browser_name')
    # Берем язык из аргумента командной строки "language" и
    # присваиваем его "user"
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        from selenium.webdriver.chrome.options import Options
        print('\nstart browser for test..')
        # Настраиваем Гугл Хрому возможность брать язык
        # пользователя из командной строки 
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nstart browser for test..')
        # Настраиваем Фаерфоксу возможность брать язык
        # пользователя из командной строки 
        firefox_options = webdriver.FirefoxProfile()
        firefox_options.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=firefox_options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    # Настраиваем ожидания
    browser.implicitly_wait(5)
    yield browser
    print('\nquit browser..')
    browser.quit()
