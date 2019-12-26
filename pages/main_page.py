''' импортируем класс из файла base_page '''
from pages.base_page import BasePage 

from selenium.webdriver.common.by import By

''' наследуем методы класса BasePage в новый класс MainPage
    таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка ''' 
class MainPage(BasePage):                                                                                 
    
    ''' функция проверяет наличие ссылки для перехода на страницу регистрации/авторизации
        в случае отсутствия ссылки, выводится сообщение об ошибке '''
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

    ''' функция осуществляет переход на страницу регистрации/авторизации '''                                                                                                          
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()