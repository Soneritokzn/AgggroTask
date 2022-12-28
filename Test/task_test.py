import time
from Pages.task_page import TaskPage
from Test.form_test import TestFormPage


class TestTask(TestFormPage):

   

    def test_task(self, driver):
        task_page = TaskPage(driver, "https://stage2.agggro.private/tasks")
        task_page.open()
        taskname, taskbody = TaskPage.create_task_save()

        time.sleep(40)