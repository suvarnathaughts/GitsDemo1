from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://selenium.dev/')
browser.maximize_window()
browser.minimize_window()
browser.refresh()
browser.close()
