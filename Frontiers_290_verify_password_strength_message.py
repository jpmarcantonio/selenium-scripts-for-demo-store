"""
An automation script to verify the password strength messages on the 'My account' page of the demo store. The script
inputs possible user passwords of varying strength (short, weak, medium, and strong) and checks that the displayed
message matches the expected message. It uses provided test data to input the password and to verify the corresponding
password strength message.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPasswordStrengthMessage:

    url = 'http://demostore.supersqa.com/my-account/'

    test_data = {
        'short_password': {
            'password': 'pw',
            'expected_msg': 'Very weak - Please enter a stronger password.'
        },
        'weak_password': {
            'password': 'passw',
            'expected_msg': 'Weak - Please enter a stronger password.'
        },
        'medium_password': {
            'password': 'MedP4ssWd',
            'expected_msg': 'Medium'
        },
        'strong_password': {
            'password': 'StR0nGp4AsSw0Rd',
            'expected_msg': 'Strong'
        }
    }

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        self.text_locator = (By.XPATH, '//*[@id="customer_login"]/div[2]/form/p[2]/span/div')

    def go_to_my_account_page(self):
        self.driver.get(self.url)
        time.sleep(2)  # sleep to load password strength check JS

    def find_and_clear_password_field(self):
        field = self.driver.find_element(By.ID, 'reg_password')
        field.clear()
        return field

    def test_password_strength(self, password_type):
        field = self.find_and_clear_password_field()
        password = self.test_data[password_type]['password']
        expected_msg = self.test_data[password_type]['expected_msg']

        field.send_keys(password)

        element = self.wait.until(EC.visibility_of_element_located(self.text_locator))

        if element.text == expected_msg:
            print(f'PASS {expected_msg}')
        else:
            raise Exception(f"Error: Password strength message is not as expected. "
                            f"Expected message '{expected_msg}', Displayed message: '{element.text}'")

    def main(self):
        self.go_to_my_account_page()

        for password_type in self.test_data:
            self.test_password_strength(password_type)

        self.driver.quit()

if __name__ == '__main__':
    obj = TestPasswordStrengthMessage()
    obj.main()