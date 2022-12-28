import time

from Pages.form_page import FormPage


class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, "https://stage2.agggro.private/login")
        form_page.open()
        username, password = form_page.fill_fields_submit()

        time.sleep(10)

