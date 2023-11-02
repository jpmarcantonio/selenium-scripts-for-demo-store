"""
Write a selenium script that will verify an invalid coupon code will show an error in the cart page.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def add_1_item_to_cart():
    driver.find_element(By.CLASS_NAME, 'add_to_cart_button').click()
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="site-header-cart"]/li[1]/a/span[2]'), '1 item')
    )
def click_cart_in_top_menu():
    driver.find_element(By.XPATH, '//*[@id="site-header-cart"]/li[1]/a/span[2]').click()

def input_invalid_coupon_and_hit_enter(invalid_coupon_code):
    coupon_field = wait.until(EC.visibility_of_element_located((By.ID, 'coupon_code')))
    coupon_field.send_keys(invalid_coupon_code)
    coupon_field.send_keys(Keys.ENTER)

def verify_error_messgae_displayed():
    coupon_error = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="post-7"]/div/div/div[1]/ul')))
    if coupon_error.is_displayed():
        print('PASS')
    else:
        raise Exception("The Error message is not displayed")

def verify_error_message_matches_expected():
    coupon_error = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="post-7"]/div/div/div[1]/ul')))
    displayed_error = coupon_error.text
    assert displayed_error == expected_error, "The displayed error does not match the expected error."


if __name__ == '__main__':

    invalid_coupon_code = "NotACoupon"
    expected_error = 'Coupon "notacoupon" does not exist!'

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get('http://localhost:8888/mysite2/')

    add_1_item_to_cart()
    click_cart_in_top_menu()
    input_invalid_coupon_and_hit_enter(invalid_coupon_code)
    verify_error_messgae_displayed()
    verify_error_message_matches_expected()
    driver.quit()