from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.about_us_link = page.locator('//*[@id="rec573054532"]/div/div/div[6]/a')
        self.projects_link = page.locator('//*[@id="rec573054532"]/div/div/div[8]/a')
        self.reviews_link = page.locator('//*[@id="rec573054532"]/div/div/div[11]/a')
        self.contacts_link = page.locator('//*[@id="rec573054532"]/div/div/div[9]/a')
        self.services_link = page.locator('//*[@id="rec573054532"]/div/div/div[7]/a')

    def click_about_us(self):
        self.about_us_link.click()

    def click_contacts(self):
        self.contacts_link.click()
    
    def click_services(self):
        self.services_link.click()
    
    def click_projects(self):
        self.projects_link.click()

    def click_reviews(self):
        self.reviews_link.click()