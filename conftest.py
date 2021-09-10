import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default=None, help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
	language_name = request.config.getoption("language")
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
	browser = webdriver.Chrome(options=options)
	#browser = webdriver.Chrome(r"D:\chromedriver\chromedriver.exe",options=options)
	yield browser
	# этот код выполнится после завершения теста
	print("\nquit browser..")
	browser.quit()
#