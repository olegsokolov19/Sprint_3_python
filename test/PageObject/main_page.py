class MainPage:
    URL = "https://stellarburgers.nomoreparties.site/"

    # кнопка "Войти" на главной странице
    button_login_on_main_page = ".//div[@class='BurgerConstructor_basket__container__2fUl3 mt-10'] / button[text()='Войти в аккаунт']"

    # кнопки "Булки", "Соусы" и "Начинки"
    burger_contents_buttons = ".//section[@class='BurgerIngredients_ingredients__1N8v2'] / .//div[contains(@class, 'tab_tab__1SPyG')]"

