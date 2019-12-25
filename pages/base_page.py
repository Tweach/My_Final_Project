class BasePage():
    def __init__(self, browser, url): #__init__ - это конструктор — метод, который вызывается, когда мы создаем объект
        self.browser = browser        # в качестве параметра передаем экземпляр драйвера
        self.url = url                # и url
    def open(self):                   # добавим еще один метод open, открывающий страницу, используя метод get()
        self.browser.get(self.url)