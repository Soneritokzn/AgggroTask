from Pages.base_page import BasePage
from Locators.task_page_locators import TaskPageLocators as TaskLocators


class TaskPage(BasePage):
    def create_task_save(self):
        taskname = "Zadacha"
        taskbody = "Testovaya"
        self.element_is_visible(TaskLocators.ADD_BUTTON).click()
        self.element_is_visible(TaskLocators.TASK_NAME).send_keys(taskname)
        self.element_is_visible(TaskLocators.TASK_BODY).send_keys(taskbody)
        self.element_is_visible(TaskLocators.SAVE_BUTTON).click()
