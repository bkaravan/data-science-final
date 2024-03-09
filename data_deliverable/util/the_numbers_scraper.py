import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def setup_driver():
    options = Options()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def scrape_data(urls, file_path, columns, i=0):
    with setup_driver() as driver:
        while i < len(urls):
            try:
                driver.get(urls[i])
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "data"))
                )
                soup = BeautifulSoup(driver.page_source, "html.parser")
                data = []
                for row in soup.find("table").find_all("tr")[1:]:
                    data.append([td.text.strip() for td in row.find_all("td")])
                df = pd.DataFrame(data, columns=columns)
                df.to_csv(file_path, mode="a", header=False, index=False)

                print(f"Scraped: {urls[i]}"), sleep(5)
                i += 1
            except Exception as e:
                print(f"Timeout: {urls[i]}"), sleep(10)


def main(start=4401, end=10001):
    base_url = "https://www.the-numbers.com/movie/budgets/all/"
    urls = [base_url + str(i) for i in range(start, end, 100)]
    file_path = "../raw_data/the_numbers/movie_budgets.csv"
    scrape_data(
        urls,
        file_path,
        columns=[
            "Rank",
            "Release Date",
            "Movie",
            "Production Budget",
            "Domestic Gross",
            "Worldwide Gross",
        ],
    )


if __name__ == "__main__":
    main()
