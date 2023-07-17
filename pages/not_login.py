from selene.support.shared import browser

from pages.users import Users


class NotLogin:

    def open (self):
        browser.open('https://imagine-club.com/')
        return self

    def finde_lp(self, name):
        browser.element("#edit-search-api-views-fulltext").type(name).press_enter()
        return self

    def lp_on_page(self):
        browser.element('#commerce-cart-add-to-cart-form-86089').click()
        return self

    def buy_not_logo(self):
        browser.element("#block-commerce-popup-cart-commerce-popup-cart").click()
        browser.element('#edit-checkout').click()
        return self

    def buy_name(self, user: Users):
        browser.element('#edit-account-login-mail').type(user.email)
        browser.element("#edit-customer-profile-billing-field-phone-und-0-value").type(user.phone)
        browser.element('#edit-continue').press_enter()
        browser.element('#edit-continue').press_enter()
        return self
