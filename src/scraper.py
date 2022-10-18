import pandas as pd
from os import environ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from temp import productItems
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from amazoncaptcha import AmazonCaptcha

HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

def chrome_initialization():
    environ['PATH'] += r'C:/SeleniumDrivers/chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return chrome_options


def get_items(driver, item):
    item_names = driver.find_elements(By.XPATH, r'//div[starts-with(@data-cel-widget,"search_result")]//descendant::h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]//child::a//child::span')
    
    item_prices = driver.find_elements(By.XPATH, r'//div[starts-with(@data-cel-widget,"search_result")]//descendant::div[@class="a-section"]//descendant::div[@class="a-row a-size-base a-color-base"]//descendant::span[@class="a-price"]//descendant::span[@class="a-price-whole"]')
    
    item_links = driver.find_elements(By.XPATH, r'//div[starts-with(@data-cel-widget,"search_result")]//descendant::h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]//child::a')

    # try: ProductItems  = pd.DataFrame([item_names, item_prices, item_links], columns=['Name', 'Price', 'Link'])
    # except: pass
    
    print(productItems)
    return productItems
    
    
def lookup_item(item) -> pd.DataFrame:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_initialization())
    driver.get(r'https://www.amazon.in/')

    # solve captcha if available
    try:
        captcha = AmazonCaptcha.fromdriver(driver)
        solution = captcha.solve()
        driver.find_element(By.ID, r'captchacharacters').send_keys(solution)
        driver.find_element(By.CLASS_NAME, r'a-button-text').click()
        print(driver.current_url)
    except: pass

    # search for item
    driver.find_element(By.ID, r'twotabsearchtextbox').send_keys(item)
    driver.find_element(By.ID, r'nav-search-submit-button').click()

    # selct 4+ stars products
    driver.find_element(By.XPATH, r'//section[@aria-label="4 Stars & Up"]').click()

    # get items from 1st page of results
    return get_items(driver, item)


if __name__ == '__main__':
    item = input("Item to search: ")
    lookup_item(item)
