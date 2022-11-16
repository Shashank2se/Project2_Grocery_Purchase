import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import Method_Module


service_obj = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

logger = logging.getLogger(__name__)
filehandler = logging.FileHandler("logfile.log")
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.setLevel(logging.DEBUG)


#------ Clearing Cart ----------
def test_cart_clear():
    Method_Module.clear_cart(driver, logger)


#------- items search and add to cart ---------
def test_add_to_cart():
    Method_Module.item_add(driver, logger)


#-------- check cost of product and verify --------
def test_cost_addition():
    Method_Module.discount_cost(driver, logger)
