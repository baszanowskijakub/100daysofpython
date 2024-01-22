import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By

SIMILAR_ACCOUNT = "londonappbrewery"
EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"

class InstaFollower:
    def __init__(self):
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(edge_options)

    def login(self):
        url = "https://www.instagram.com/"
        cookies_xpath = '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]'
        email_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        login_xpath = '//*[@id="loginForm"]/div/div[3]'
        save_xpath = "//div[contains(text(), 'Not now')]"
        notification_xpath = "//button[contains(text(), 'Not Now')]"

        self.driver.get(url)

        cookies = self.driver.find_element(By.XPATH, value=cookies_xpath)
        cookies.click()

        email = self.driver.find_element(By.XPATH, value=email_xpath)
        email.send_keys(EMAIL)

        password = self.driver.find_element(By.XPATH, value=password_xpath)
        password.send_keys(PASSWORD)

        time.sleep(2.1)
        log_in = self.driver.find_element(By.XPATH, value=login_xpath)
        log_in.click()

        time.sleep(10)
        save_login_prompt = self.driver.find_element(by=By.XPATH, value=save_xpath)
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)
        notifications_prompt = self.driver.find_element(by=By.XPATH, value=notification_xpath)
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(8.2)
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(4)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()



