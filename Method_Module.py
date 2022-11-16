import time
from selenium.webdriver.common.by import By
import Elements_PO

actualList = []


def clear_cart(driver, logger):
    # try:
        Elements_PO.cart_open(driver)
        logger.info("cart option is opened")
        products = Elements_PO.cart_products(driver)
        number = Elements_PO.product_number(driver)
        logger.info(f"Number of products in cart = {number}")
        if len(products) > 0:
            for product in products:
                Elements_PO.cart_product_delete(driver)
                time.sleep(1)
        verify = Elements_PO.verify_empty_cart(driver)
        assert "cart is emptty" in verify             #---- empty word written wrong for assertion error..-----
        logger.info(verify)
    # except Exception as e:
    #     print(e)
    #     logger.error("Exception raised")
    #     logger.error("cart not empty -> sentence not found, Check code again")


def item_add(driver, logger):
    try:
        Elements_PO.cart_open(driver)
        Elements_PO.search_c(driver)
        logger.info("Search letter C within product word")
        time.sleep(2)
        products = Elements_PO.products_letter_c(driver)
        count = len(products)
        logger.info(f"Number of products in matched with letter C = {count}")
        # print(count)
        assert count > 0
        for product in products:
            actualList.append(product.find_element(By.XPATH, "h4").text)
            print(product.find_element(By.XPATH, "h4").text)
            product.find_element(By.XPATH, "//button[contains(text(), 'ADD TO CART')]").click()

        logger.info("All product word contain letter C added to cart")
        assert "Carrot - 1 Kg" in actualList
        logger.info("Assertion Pass = word Carrot found in actual list")
    except Exception as e:
        print(e)
        logger.error("Assertion Fail = word Carrot not found in actual list, /n Check code again")
        # print("carrot not added in cart")


def discount_cost(driver, logger):
    try:
        Elements_PO.cart_open(driver)
        logger.info("Cart open")
        Elements_PO.proceed_to_checkout(driver)
        costs = Elements_PO.products_cost(driver)
        sum = 0
        print(len(costs))
        for cost in costs:
            sum = sum + int(cost.text)
        # print(sum)
        logger.info(f"Cost addition of all products = {sum}")
        total = Elements_PO.total_amount(driver)
        assert sum == total
        logger.info("Cost addition of all products is correct")
        Elements_PO.promo_code(driver)
        Elements_PO.apply_promocode(driver)
        time.sleep(10)
        per = Elements_PO.discount_percentage(driver)
        discount = Elements_PO.discount_cost(driver)
        assert total > discount
        logger.info(f"Discount percentage = {per}")
        logger.info(f"After discount cost = {discount}")

    except Exception as e:
        print(e)
        logger.error(f"Discount not applied, Check code again")
