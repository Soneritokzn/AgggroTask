from selenium.webdriver.common.by import By


class FormPageLocators():
    LOGIN_FORM = (By.XPATH, "//a[@class='link--K8aqB loginForm__link--JSKIx']")
    USERNAME = (By.XPATH, "//input[@type='text']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT = (By.XPATH, "//span[@class='MuiButton-label']")
