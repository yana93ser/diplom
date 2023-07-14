import allure

from pages.not_login import NotLogin
from pages.users import test_user



# @allure.step('Покупка виниловой пластинки без регистрации на сайте')
def test_not_login(setup_browser):
    browser = setup_browser
    not_login = NotLogin()

    with allure.step("Открыть страницу магазина"):
        browser.open('https://imagine-club.com/')
