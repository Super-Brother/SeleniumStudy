from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome('D:\Python\chromedriver.exe')
    browser.get('https://www.baidu.com')
    search_box = browser.find_element_by_id('kw')
    search_box.send_keys('python')
    submit_button = browser.find_element_by_id('su')
    submit_button.click()