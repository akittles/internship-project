from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
# from appium import webdriver
# from appium.options.android import UiAutomator2Options


from app.application import Application
from support.logger import logger


def browser_init(context,scenario_name):
    """
    :param context: Behave context
    # """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.app = Application(context.driver)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    ######FIREFOX BROWSWER, THIS ALSO WORKED IN HEADLESS MODE########
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###--old way of doing things,
    #           #Not needed but a second option
    # driver_path = GeckoDriverManager().install()
    # service = Service(executable_path='C:/Users/Owner/Desktop/internship-project/geckodriver-v0.35.0-win32'
    #                                   '/geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)

    # context.driver = webdriver.Safari() #CAN ONLY RUN ON MAC OR IOS

    ### HEADLESS MODE #### TESTING IN THE TERMINAL
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )



    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'anthonykittles_DMlABu'
    bs_key = 'UUbrpL7fPHuFFe9Y7zo4'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "os": "Windows",
        "osVersion": "11",
        'browserName': 'chrome',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15) # aka explicit wait

    context.app = Application(context.driver)

# ----------------MOBILE TESTING---------------------------


# def mobile_driver_init(context, scenario_name):
#     """
#     :param context: Behave context
#     """
#     desired_capabilities = {
#         "platformName": "Android",
#         "automationName": 'uiautomator2',
#         "platformVersion": "15",
#         "deviceName": "Android Emulator",
#         "appActivity": "org.wikipedia.main.MainActivity",
#         "appPackage": "org.wikipedia",
#         # Put your path below:
#         "app": "C:/Users/Owner/mobile_app/mobile_app/wikipedia.apk"
#         # "app": ".../mobile_app/wikipedia.apk"
#
#     }
#
#     appium_server_url = 'http://localhost:4723'
#     capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
#
#     context.driver = webdriver.Remote(appium_server_url, options=capabilities_options)
#     context.driver.implicitly_wait(5)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'\nStarted step: {step.name}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'\nStep failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
