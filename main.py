
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(browser):
    browser.get("https://youtube.com/signin")
    time.sleep(3)
    email = browser.find_element_by_css_selector("[type = 'email']")
    next1 = browser.find_element_by_css_selector("button[jsname= 'LgbsSe']")


    email.send_keys("testmail02012001@gmail.com")
    time.sleep(3)
    next1.click()
    time.sleep(3)
    password = browser.find_element_by_css_selector("[type='password']")
    next2 = browser.find_element_by_css_selector("button[jsname = 'LgbsSe']")

    password.send_keys("password0201!")
    next2.click()

    time.sleep(10)
    video = browser.find_element_by_css_selector("yt-formatted-string[id = 'video-title']")
    video.click()

    while True:

        time.sleep(4)

        browser.execute_script('window.scrollTo(0, 600);')

        time.sleep(3)

        comment = browser.find_element_by_css_selector("div[id = 'placeholder-area']")
        comment.click()
        time.sleep(5)
        commentIt = browser.find_element_by_css_selector("div[id = 'contenteditable-root']")

        commentIt.send_keys(":)")

        commentIt.send_keys(Keys.CONTROL, Keys.ENTER)

        time.sleep(5)

        browser.execute_script('window.scrollTo(0, -600);')

        time.sleep(4)

        NextVid = browser.find_element_by_css_selector("a[aria-label = 'Next (SHIFT+n)']")
        NextVid.send_keys(Keys.SHIFT, 'n')


        time.sleep(4)




def main():
    browser = webdriver.Firefox()
    login(browser)


main()