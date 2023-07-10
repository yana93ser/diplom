import allure

from pages.not_login import NotLogin
from pages.users import test_user


# @allure.step('Покупка виниловой пластинки без регистрации на сайте')
def test_not_login():
    not_login = NotLogin()

    with allure.step("Открыть страницу магазина"):
        not_login.open()
    with allure.step("Ввести в поле поиска исполнителя"):
        not_login.finde_lp("sinatra frank")
    with allure.step("Поиск необходимой пластинки на сайте"):
        not_login.lp_on_page()
    with allure.step("Покупка пластинки незарегистрированным пользователем"):
        not_login.buy_not_logo()


    with allure.step("Подтверждение покупки"):
        not_login.buy_name(test_user)

