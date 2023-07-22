"""
Write a selenium script to test that the user registration field works on our demo store.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random


class VerifyNewUserRegistration:

    url = 'http://demostore.supersqa.com/my-account/'

    def __init__(self):
        self.rand_email = None
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def go_to_my_account_page(self):
        self.driver.get(self.url)

    def generate_random_email(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(15))
        self.rand_email = rand_string + '@supersqa.com'

    def find_register_email_field(self):
        field = self.driver.find_element(By.ID, 'reg_email')
        field.send_keys(self.rand_email)

    def enter_password(self):
        field = self.driver.find_element(By.ID, 'reg_password')
        field.send_keys('MyPassword12345!!')

    def click_register(self):
        register_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[value ="Register"]')
        register_btn.click()

    def verify_account_created(self):
        try:
            self.driver.find_element(By.XPATH, '//*[@id="post-9"]/div/div/nav/ul/li[6]/a')
            print('PASS')
        except:
            raise Exception('User registration failed. The user was not logged in after registration.')


    def main(self):
        self.go_to_my_account_page()
        self.generate_random_email()
        self.find_register_email_field()
        self.enter_password()
        self.click_register()
        self.verify_account_created()
        self.driver.quit()


if __name__ == '__main__':

    obj = VerifyNewUserRegistration()
    obj.main()