import logging

from selenium.webdriver.common.by import By


def product_number(driver):
    num = int(driver.find_element(By.XPATH, "//div[@class='cart-info']//tr[1]//td[3]").text)
    return num

def search_bar(driver):
    driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").click()


def search_c(driver):
    driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").send_keys("c")


def search_click(driver):
    driver.find_element(By.XPATH, "//button[@class='search-button']").click()


def cart_open(driver):
    driver.find_element(By.XPATH, "//img[@alt='Cart']").click()


def cart_products(driver):
    products = driver.find_elements(By.XPATH, "//div[@class='cart-preview active']//a[@class='product-remove']")
    return products


def cart_product_delete(driver):
    driver.find_element(By.XPATH, "//div[@class='cart-preview active']//a[@class='product-remove']").click()


def verify_empty_cart(driver):
    num = driver.find_element(By.XPATH, "//div[@class='empty-cart']/h2[contains(text(), 'You cart is empty!')]").text
    return num


def products_letter_c(driver):
    product = driver.find_elements(By.XPATH, "//div[@class='product']")
    return product


def proceed_to_checkout(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()


def products_cost(driver):
    costs = driver.find_elements(By.XPATH, "//tbody//tr//td[5]")
    return costs


def total_amount(driver):
    amount = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
    return amount


def promo_code(driver):
    driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")


def apply_promocode(driver):
    driver.find_element(By.XPATH, "//button[normalize-space()='Apply']").click()


def discount_percentage(driver):
    perc = driver.find_element(By.XPATH, "//span[@class='discountPerc']").text
    return perc


def discount_cost(driver):
    discount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)
    return discount