from selenium import webdriver

count = 0

if count == 0:
    count = 1
    driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    if count == 1:
        print(driver.page_source)
