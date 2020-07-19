from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH="./chromedriver"
SOURCE_URL="https://sfbay.craigslist.org/d/apts-housing-for-rent/search/apa"
options = Options()
options.headless = True

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(SOURCE_URL)
print(driver.page_source)
driver.quit()