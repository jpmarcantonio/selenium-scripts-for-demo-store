"""
Write a selenium script to test that the password strength message is as expected. This is testing a weak password.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPasswordStrengthMessage:

    url = 'http://demostore.supersqa.com/my-account/'

    test_data = {
            'username': 'user_mail_test@gmail.com',
            'short_password': 'pw',
            'weak_password': 'passw',
            'medium_password': 'MedP4ssWd',
            'strong_password': 'StR0nGp4AsSw0Rd',
            'expected_msg_short': 'Very weak - Please enter a stronger password.',
            'expected_msg_weak': 'Weak - Please enter a stronger password.',
            'expected_msg_med': 'Medium',
            'expected_msg_strong': 'Strong'
        }

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        self.text_locator = (By.XPATH, '//*[@id="customer_login"]/div[2]/form/p[2]/span/div')

    def go_to_my_account_page(self):
        self.driver.get(self.url)
        time.sleep(2)  # sleep to load password strength check JS

    def find_register_email_field(self):
        self.driver.find_element(By.ID, 'reg_email').send_keys(self.test_data['username'])

    def test_short_password(self):
        field = self.driver.find_element(By.ID, 'reg_password')
        field.clear()
        field.send_keys(self.test_data['short_password'])

        element = self.wait.until(EC.visibility_of_element_located(self.text_locator))

        if element.text == self.test_data['expected_msg_short']:
            print('PASS Short')
        else:
            raise Exception(f"Error: Password strength message is not as expected. "
                            f"Expected message: '{self.test_data['expected_msg_short']}', Displayed message: '{element.text}'")

    def test_weak_password(self):
        field = self.driver.find_element(By.ID, 'reg_password')
        field.clear()
        field.send_keys(self.test_data['weak_password'])

        element = self.wait.until(EC.visibility_of_element_located(self.text_locator))

        if element.text == self.test_data['expected_msg_weak']:
            print('PASS Weak')
        else:
            raise Exception(f"Error: Password strength message is not as expected. "
                            f"Expected message: '{self.test_data['expected_msg_weak']}', Displayed message: '{element.text}'")

    def test_medium_password(self):
        field = self.driver.find_element(By.ID, 'reg_password')
        field.clear()
        field.send_keys(self.test_data['medium_password'])

        element = self.wait.until(EC.visibility_of_element_located(self.text_locator))

        if element.text == self.test_data['expected_msg_med']:
            print('PASS Medium')
        else:
            raise Exception(f"Error: Password strength message is not as expected. "
                            f"Expected message: '{self.test_data['expected_msg_med']}', Displayed message: '{element.text}'")

    def test_strong_password(self):
        field = self.driver.find_element(By.ID, 'reg_password')
        field.clear()
        field.send_keys(self.test_data['strong_password'])

        element = self.wait.until(EC.visibility_of_element_located(self.text_locator))

        if element.text == self.test_data['expected_msg_strong']:
            print('PASS Strong')
        else:
            raise Exception(f"Error: Password strength message is not as expected. "
                            f"Expected message: '{self.test_data['expected_msg_strong']}', Displayed message: '{element.text}'")

    def main(self):
        self.go_to_my_account_page()
        self.find_register_email_field()
        self.test_short_password()
        self.test_weak_password()
        self.test_medium_password()
        self.test_strong_password()
        self.driver.quit()


if __name__ == '__main__':

    obj = TestPasswordStrengthMessage()
    obj.main()