from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# from appium.options import
#
# from time import sleep
#
# desired_capabilities = {
#     "platformName": "Android",
#     "automationName": 'uiautomator2',
#     "platformVersion": "15",
#     "deviceName": "Android Emulator",
#     "appActivity": "org.wikipedia.main.MainActivity",
#     "appPackage": "org.wikipedia",
#     # Put your path below:
#     "app": "C:/Users/Owner/python-appium-automation/mobile_app/wikipedia.apk"
# }
#
# appium_server_url = 'http://localhost:4723'
# capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
#
# driver = webdriver.Remote(appium_server_url, options=capabilities_options)
# driver.implicitly_wait(5)