''' импортируем возможное исключение (NoSuchElementException возникает при отсутствии элемента на странице)
    сама проверка находится в файле main_page '''
from selenium.common.exceptions import NoSuchElementException

class BasePage():

    ''' __init__ — конструктор — метод, который вызывается при создании объекта '''
    def __init__(self, browser, url):       
        ''' в качестве параметров передаем экземпляр драйвера и url '''
        self.browser = browser        
        self.url = url                
    
    ''' метод open открывает страницу, используя метод get() '''
    def open(self):                   
        ''' браузер является аргументом в классе BasePage, поэтому обращение к нему происходит с помощью self() '''
        self.browser.get(self.url)    

    ''' передаем в конструктор в качестве параметров экземпляр драйвера и url; сохраняем эти данные как атрибуты класса '''
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    ''' реализация проверки элемента на странице и перехвата возможного исключения
        аргументы how, what: как искать (css, id, xpath и тд) и что искать (строку-селектор) '''
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True