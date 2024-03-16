from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser .........")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser .........")
    return driver 

def pytest_addoption(parser):                       #this will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                              #this will return the browser value to setup method
    return request.config.getoption("--browser")

# pytest HTML Report
# It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config.option.custom_metadata = {
        'Project Name': 'Hybrid Framework',
        'Module Name': 'Customers',
        'Tester': 'Himanshu'
    }

# It is a hook to delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

