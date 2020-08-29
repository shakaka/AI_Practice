# autoplay 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('htte://habrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.LEFT)
