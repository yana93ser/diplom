import allure

from pages.not_login import NotLogin
from pages.users import test_user



# @allure.step('Покупка виниловой пластинки без регистрации на сайте')
def test_not_login(setup_browser):
    browser = setup_browser
    not_login = NotLogin()

    with allure.step("Открыть страницу магазина"):
        not_login.open()
        browser.element("#edit-search-api-views-fulltext").type('sinatra').press_enter()
        browser.element('#commerce-cart-add-to-cart-form-86089').click()
        browser.element("#block-commerce-popup-cart-commerce-popup-cart").click()
        browser.element('#edit-checkout').click()