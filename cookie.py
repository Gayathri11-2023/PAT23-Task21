from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class loginPage:
    # constructor method
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    # Get the url and boot the driver
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)
   # Quit from the driver
    def quit(self):
        self.driver.quit()
    # Login into url site
    def login(self):
        username_input = self.driver.find_element(by=By.ID, value="user-name")
        password_input = self.driver.find_element(by=By.ID,  value="password")
        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        self.driver.find_element(by=By.ID, value= "login-button").click()
        sleep(5)
    # Get the cookies from the driver
    def getCookies(self):
        return self.driver.get_cookies()
    # get the  Current url
    def getCurrent_URL(self):
        return self.driver.current_url

url = "https://www.saucedemo.com/"
obj = loginPage(url)
obj.boot()
# Get the cookies Before login 
print(obj.getCookies())
print(obj.getCurrent_URL())
obj.login()
# Get the cookies after login
print(obj.getCookies())
obj.quit()



