from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from QueryModel import QueryModel

SOURCE_URL = "https://sfbay.craigslist.org/d/apts-housing-for-rent/search/apa"

class Scraper:
    def __init__(self, driver_path, model_src):
        self.driver_path = driver_path
        self.query_model = QueryModel(model_src)
    
    def scrape(self):
        options = Options()
        options.headless = True

        driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        driver.get(SOURCE_URL)
        print(driver.page_source)
        driver.quit()