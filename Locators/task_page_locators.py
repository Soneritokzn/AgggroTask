from selenium.webdriver.common.by import By


class TaskPageLocators():
    ADD_BUTTON = (By.XPATH, "//span[contains(text(),'Добавить')]")
    TASK_NAME = (By.XPATH,
                            "//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-fullWidth MuiInputBase-formControl']//input[@type='text']")
    TASK_BODY = (By.XPATH,
                            "//body[@style='overflow: hidden;']/div[@class='MuiDialog-root taskCreateModal--fMs_f']/div[@class='MuiDialog-container MuiDialog-scrollPaper']/div[@class='MuiPaper-root MuiDialog-paper taskCreateModal__window--3nOex MuiDialog-paperScrollPaper MuiDialog-paperWidthFalse MuiDialog-paperFullWidth MuiPaper-elevation24 MuiPaper-rounded']/div[@class='agggro scrollContainer']/form/div[@class='MuiDialogContent-root']/div[@class='formField--fhG20 taskCreateModal__formRow--VfqQd fullWidth--r_r4o']/div[@class='formField__input--ipKjU']/div[@class='MuiInputBase-root MuiOutlinedInput-root textarea--V31Md MuiInputBase-fullWidth MuiInputBase-multiline MuiOutlinedInput-multiline MuiInputBase-adornedEnd MuiOutlinedInput-adornedEnd']/textarea[1]")
    SAVE_BUTTON = (By.XPATH,
                            "//button[@type='submit']//span[@class='MuiButton-label'][contains(text(),'Сохранить')]")
    TASK_HEADER = (By.XPATH,
                                   "//a[@class='MuiTypography-root MuiLink-root MuiLink-underlineAlways MuiTypography-colorPrimary']")






