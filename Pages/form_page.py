from Locators.form_page_locators import FormPageLocators as Locators

from Pages.base_page import BasePage


class FormPage(BasePage):

    def fill_fields_submit(self):
        username = "sales-user"
        password = "123login123"
        self.element_is_visible(Locators.LOGIN_FORM).click()
        self.element_is_visible(Locators.USERNAME).send_keys(username)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.SUBMIT).click()
        return username, password

