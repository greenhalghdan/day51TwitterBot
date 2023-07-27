import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By

import os

TWITTER_USERNAME = os.environ.get("username")
TWITTER_PASSWORD = os.environ.get("password")
class InternetSpeedTwitterBot():
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_web_driver = Service(r"C:\Users\green\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.chrome_web_driver)
        self.driver.maximize_window()
        self.PROMISED_DOWN = 100
        self.PROMISED_UP = 10

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        accept_cookies = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        accept_cookies.click()
        time.sleep(2)
        start_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        start_button.click()
        time.sleep(50)
        self.downloadspeed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.downloadspeed = self.downloadspeed.text
        self.upload_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.upload_speed = self.upload_speed.text
        print(self.upload_speed)
        print(self.downloadspeed)
    def tweet_at_provider(self):
        if self.upload_speed < self.PROMISED_UP or self.downloadspeed < self.PROMISED_UP:
            self.driver.get("https://twitter.com/i/flow/login?redirect_after_login=%2F")
            time.sleep(10)
            username = self.driver.find_element(By.NAME, value="text")
            username.send_keys(TWITTER_USERNAME)
            time.sleep(1)
            submit_username = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
            submit_username.click()
            time.sleep(1)
            password = self.driver.find_element(By.NAME, value="password")
            password.send_keys(TWITTER_PASSWORD)
            login_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
            login_button.click()
            time.sleep(5)
            time.sleep(2)
            tweet_cookie = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]')
            tweet_cookie.click()
            time.sleep(2)
            tweet_inputt = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]')
            tweet_inputt.click()
            time.sleep(2)
            tweet_input = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            time.sleep(2)
            tweet_input.send_keys(f"Hello internetProviderNameHere it seem i am having speed issues. I am currently getting a speed of {self.upload_speed} upload and {self.downloadspeed} down")
            time.sleep(2)
            send_tweet = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
            send_tweet.click()
            time.sleep(60)
speedtest = InternetSpeedTwitterBot()

speedtest.get_internet_speed()
speedtest.tweet_at_provider()
#