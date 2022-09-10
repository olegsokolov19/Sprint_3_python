class RegistrationPage:
    URL = 'https://stellarburgers.nomoreparties.site/register'

    # поля для регистрации пользователя (имя, почта, пароль)
    fields_registration_form = ".//div[@class='input__container'] / .//input[@class='text input__textfield text_type_main-default']"

    # кнопка "Зарегистрироваться"
    registration_button = ".//button[text()='Зарегистрироваться']"

    # кнопка "Войти"
    button_login_in_registration_form = "Auth_link__1fOlj"

    # ошибка при вводе некорректного пароля
    invalid_password_error = ".//div[@class='input__container'] / p[@class='input__error text_type_main-default']"