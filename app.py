from Scraper import Scraper

DRIVER_PATH = "./chromedriver"
SOURCE_URL = "https://sfbay.craigslist.org/d/apts-housing-for-rent/search/apa"
MODEL_SRC = "./queryModelSample.json"

def main():
    scraper = Scraper(DRIVER_PATH, MODEL_SRC)
    print("hello")

if __name__ == "__main__":
    main()