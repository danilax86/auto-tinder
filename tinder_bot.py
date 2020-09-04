import os
import time

from web_driver import WebDriver
from selenium import webdriver
from selenium.common.exceptions import *

webDriverOptions = WebDriver()


class TinderBot:
    def __init__(self):
        if os.name == "posix":
            self.driver = webdriver.Firefox(options=webDriverOptions.get_options())
        if os.name == "nt":
            self.driver = webdriver.Firefox(executable_path=r'./geckodriver.exe',
                                            options=webDriverOptions.get_options())
        self.driver.get("https://tinder.com/")

    def login(self, login: str, password: str):
        self.google_login(login, password)

    def google_login(self, login: str, password: str):
        self.log()
        self.push_login_btn()
        self.push_login_btn()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.input_email(login)
        self.input_password(password)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.allow_location()
        self.allow_notification()

    def log(self):
        while True:
            try:
                login_btn = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button")
                login_btn.click()
                break
            except NoSuchElementException:
                time.sleep(1.5)

    def push_login_btn(self):
        while True:
            try:
                google_btn = self.driver.find_element_by_xpath(
                    "/html/body/div[2]/div/div/div/div/div[3]/span/div/div/button")
                google_btn.click()
                break
            except NoSuchElementException:
                time.sleep(1.5)

    def input_email(self, login: str):
        global continue_btn
        while True:
            try:
                email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
                email_in.send_keys(login)
                continue_btn = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div")
                continue_btn.click()
                time.sleep(1)
                # Login correctness checker
                try:
                    self.driver.find_element_by_xpath(
                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div["
                        "1]/div/form/span/section/div/div/div[1]/div/div[2]")
                    email_in.clear()
                    print("Login is incorrect.")
                    login = str(input("Please, provide correct login: "))
                    email_in.send_keys(login)
                    continue_btn.click()
                    time.sleep(1)
                except NoSuchElementException:
                    print("Login is correct.")
                break

            except NoSuchElementException:
                print("\r", end="")

    def input_password(self, password: str):
        while True:
            try:
                password_in = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div["
                    "1]/div/form/span/section/div/div/div[ "
                    "1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
                password_in.send_keys(password)
                continue_btn = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div")
                continue_btn.click()
                # Password correctness checker
                try:
                    self.driver.find_element_by_xpath(
                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]")
                    password_in.clear()
                    print("Password is incorrect.")
                    password = str(input("Please, provide correct password: "))
                    password_in.send_keys(password)
                    continue_btn.click()
                except NoSuchElementException:
                    print("Password is correct.")
                break
            except NoSuchElementException:
                print("\r", end="")

    def allow_location(self):
        while True:
            try:
                allow_location_btn = self.driver.find_element_by_xpath(
                    "/html/body/div[2]/div/div/div/div/div[3]/button[1]")
                allow_location_btn.click()
                break
            except NoSuchElementException:
                loading("user response")

    def allow_notification(self):
        while True:
            try:
                time.sleep(3)
                allow_notification_btn = self.driver.find_element_by_xpath(
                    "/html/body/div[2]/div/div/div/div/div[3]/button[2]")
                allow_notification_btn.click()
                break
            except NoSuchElementException or StaleElementReferenceException:
                loading("page loading")

    def like(self):
        while True:
            try:
                # Pushing a like button
                like_btn = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button")
                like_btn.click()
            except ElementClickInterceptedException:
                try:
                    try:
                        # Avoiding Tinder Premium notification
                        back_to_tinder = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/button[2]")
                        back_to_tinder.click()
                        try:
                            # If not enough likes
                            self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[1]")
                            print("\nYou are Out of Likes!")
                            break
                        except NoSuchElementException or ElementClickInterceptedException:
                            # If match
                            back_to_tinder = self.driver.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/main/div["
                                "2]/div/div/div[1]/div/div[3]/a")
                            back_to_tinder.click()
                    except NoSuchElementException or ElementClickInterceptedException:
                        # If not enough likes
                        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[1]")
                        print("\nYou are Out of Likes!")
                        break
                except NoSuchElementException or ElementClickInterceptedException:
                    time.sleep(1)
                    loading("partners")

    def dislike(self):
        try:
            dislike_btn = self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button")
            dislike_btn.click()
        except ElementClickInterceptedException:
            time.sleep(1)
            loading("partners")

    def auto_swipe(self):
        time.sleep(0.5)
        self.like()


def loading(obj_name: str):
    animation = ["|", "/", "-", "\\"]
    for i in animation:
        print('\rPlease wait for the ' + obj_name, i, end="")
        time.sleep(0.5)
