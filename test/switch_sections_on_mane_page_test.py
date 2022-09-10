from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from PageObject.main_page import MainPage as mp


class SwitchSectionsOnManePageTest:
    def selectSaucesSection(self):
        active_sauces_section = ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'] / .//span[text()='Соусы']"

        driver = webdriver.Chrome()
        driver.get(mp.URL)

        # нажатие по кнопке "Соусы"
        driver.find_elements(By.XPATH, mp.burger_contents_buttons)[1].click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, active_sauces_section)))

        driver.quit()

    def selectFillingsSection(self):
        active_fillings_section = ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'] / .//span[text()='Начинки']"

        driver = webdriver.Chrome()
        driver.get(mp.URL)

        # нажатие по кнопке "Начинки"
        driver.find_elements(By.XPATH, mp.burger_contents_buttons)[2].click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, active_fillings_section)))

        driver.quit()

    def selectBunsSection(self):
        active_buns_section = ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'] / .//span[text()='Булки']"

        driver = webdriver.Chrome()
        driver.get(mp.URL)

        #  "Булки" выбрана по умолчанию. Шаг с кликом на "Соусы" нужен, чтобы задизейблить кнопку "Булки"
        driver.find_elements(By.XPATH, mp.burger_contents_buttons)[1].click()

        # нажатие по кнопке "Булки"
        driver.find_elements(By.XPATH, mp.burger_contents_buttons)[0].click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, active_buns_section)))

        driver.quit()
