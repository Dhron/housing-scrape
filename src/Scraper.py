from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from QueryModel import QueryModel

class Scraper:
    def __init__(self, driver_path, model_src):
        self.driver_path = driver_path
        self.query_model = QueryModel(model_src).model
    
    def __perform_search_query(self, driver, query):
        search_bar = driver.find_element_by_id("query")
        search_bar.send_keys(query["location_query"])
        
        price_max_input = driver.find_element_by_class_name("min")
        price_max_input.send_keys(query["price_low"])
        
        price_max_input = driver.find_element_by_class_name("max")
        price_max_input.send_keys(query["price_high"])
        
        search_btn = driver.find_element_by_class_name("searchbtn")
        search_btn.click()
        
    
    def __process_search_elements(self, elements):
        for element in elements:
            price = element.find_element_by_class_name("result-price")
            link = element.find_element_by_tag_name("a").get_attribute("href")
            print(price.text)
            print(link)
    
    def scrape(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=self.driver_path)
        
        # Iterate though provided queries, and perform a scrape based on the query
        for query in self.query_model["queries"]:
            driver.get(query["source"])
            self.__perform_search_query(driver, query)
            list_elements = driver.find_elements_by_class_name("result-row")
            self.__process_search_elements(list_elements)
        driver.quit()