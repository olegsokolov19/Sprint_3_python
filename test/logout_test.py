from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from PageObject.login_page import LoginPage as lp
from PageObject.main_page import MainPage as mp
from PageObject.header_of_page import HeaderOfPage as hp
from PageObject.person_account_page import PersonAccountPage as person_account


class LogoutTest:
    def logoutOutOfPersonAccount(self):
        login = 'olegsokolov02999@yandex.ru'
        password = '30572325'

        driver = webdriver.Chrome()
        driver.get(mp.URL)

        driver.find_element(By.XPATH, mp.button_Login_on_main_page).click()

        driver.find_elements(By.CSS_SELECTOR, lp.fields_login_form)[0].send_keys(login)
        driver.find_elements(By.CSS_SELECTOR, lp.fields_login_form)[1].send_keys(password)
        driver.find_element(By.XPATH, lp.button_login_in_login_form).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, hp.personal_account_button).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, person_account.logout_button)))

        driver.find_element(By.XPATH, person_account.logout_button).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, lp.button_login_in_login_form)))

        driver.quit()
