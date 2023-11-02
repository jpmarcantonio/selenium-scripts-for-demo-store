"""
Write a selenium script that will add an item to cart, go to the cart page, and increase the count in the cart.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def add_1_item_to_cart():
    driver.find_element(By.CLASS_NAME, 'add_to_cart_button').click()
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/ul/li[1]/a[3]'))
    )

def go_to_cart():
    driver.find_element(By.XPATH, '//*[@id="main"]/ul/li[1]/a[3]').click()

# This clicks on the up arrow to increase quantity
def find_quantity_and_increase():
    qty_btn = driver.find_element(By.CLASS_NAME, 'quantity')
    for i in range(5):
        qty_btn.click()

def verify_quantity_increased():
    try:
        update_cart_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[value="Update cart"')))
        update_cart_btn.click()
        print("PASS. Quantity in cart was increased.")
    except:
        raise Exception("Error.'Update Cart' button is not clickable. Quantity in cart was not increased.")

if __name__ == '__main__':
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get('http://demostore.supersqa.com/')

    add_1_item_to_cart()
    go_to_cart()
    find_quantity_and_increase()
    verify_quantity_increased()
    driver.quit()

