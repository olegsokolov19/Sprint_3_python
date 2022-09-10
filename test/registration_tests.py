from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObject import RegistrationPage as rp
from get_random_user_data import *


class RegistrationTest:

    # Успешная регистрация
    def success_registration_test(self):
        driver = webdriver.Chrome()
        driver.get(rp.URL)

        driver.find_elements(By.XPATH, rp.fields_registration_form)[0].send_keys(get_random_name())
        driver.find_elements(By.XPATH, rp.fields_registration_form)[1].send_keys(get_random_email())
        driver.find_elements(By.XPATH, rp.fields_registration_form)[2].send_keys(get_random_password())

        driver.find_element(By.XPATH, rp.registration_button).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

        driver.quit()

    # Регистрация с некорректным паролем (длина 5 символов)
    def registration_with_incorrect_password(self):
        expected_error_text = 'Некорректный пароль'

        driver = webdriver.Chrome()
        driver.get(rp.URL)

        driver.find_elements(By.XPATH, rp.fields_registration_form)[0].send_keys(get_random_name())
        driver.find_elements(By.XPATH, rp.fields_registration_form)[1].send_keys(get_random_email())
        driver.find_elements(By.XPATH, rp.fields_registration_form)[2].send_keys(get_random_password(5))

        driver.find_element(By.XPATH, rp.registration_button).click()

        actual_error_text = driver.find_element(By.XPATH, rp.invalidPasswordError).text

        assert expected_error_text == actual_error_text

        driver.quit()
