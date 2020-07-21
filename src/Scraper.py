from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from QueryModel import QueryModel

class Scraper:
    def __init__(self, driver_path, model_src):
        self.driver_path = driver_path
        self.query_model = QueryModel(model_src)
    
    def scrape(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=self.driver_path)
        
        # Iterate though provided queries, and perform a scrape based on the query
        for query in self.query_model.model["queries"]:
            driver.get(query["source"])
            print(driver.page_source)
            driver.quit()