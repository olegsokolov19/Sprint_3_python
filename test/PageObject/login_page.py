class LoginPage:
    URL = 'https://stellarburgers.nomoreparties.site/login'

    # поля в форме авторизации
    fields_login_form = "div.input__container input"

    # кнопка "Войти" в форме авторизации
    button_login_in_login_form = ".//button[text()='Войти']"

    # кнопка "Войти" в форме сброса пароля
    button_login_in_reset_password_form = "Auth_link__1fOlj"

