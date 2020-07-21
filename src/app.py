from Scraper import Scraper

DRIVER_PATH = "../chromedriver"
MODEL_SRC = "./queryModelSample.json"

def main():
    print("--- Scraper Init ---")
    scraper = Scraper(DRIVER_PATH, MODEL_SRC)
    print("--- Scraper Run --- ")
    scraper.scrape()
    print("--- Scraper End --- ")

if __name__ == "__main__":
    main()