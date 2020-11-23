from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery

import time

KEYWORD = 'iPad'
url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)


def crawl_page(page):
    try:
        browser.get(url)

        time.sleep(5)

        if page > 1:
            page_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.input.J_Input')))
            ensure_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.btn.J_Submit')))
            page_input.clear()
            page_input.send_keys(page)
            ensure_btn.click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))

        get_product()
    except:
        crawl_page(1)


def get_product():
    html = browser.page_source
    doc = PyQuery(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('div.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)


if __name__ == '__main__':
    browser = webdriver.Chrome('D:\Python\chromedriver.exe')
    # 设置等待时间
    wait = WebDriverWait(browser, 10)

    crawl_page(1)
