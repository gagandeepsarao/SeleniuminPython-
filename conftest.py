import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
driver = None




def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:/driver/chromedriver.exe")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif browser_name== "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE Driver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


