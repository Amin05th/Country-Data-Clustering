from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException
import pandas as pd
import numpy as np
import time

path = "/home/amin/Dokumente/Python/Scikit-learn/Clustering/Country Data Clustering/chromedriver"


def fetch_country_population(countries, path):
    options = Options()
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.get("https://www.google.de/")
    driver.find_element(By.XPATH, "//*[text()='Alle akzeptieren']").click()
    country_population = []

    for country in countries:
        time.sleep(1)
        search_input = driver.find_element(By.NAME, "q")
        search_input.send_keys(country + " population")
        search_input.send_keys(Keys.ENTER)
        try:
            population_result = driver.find_element(By.CLASS_NAME, "ayqGOc").text
            country_population.append(population_result)
        except NoSuchElementException:
            country_population.append(-1)
        search_input = driver.find_element(By.NAME, "q")
        search_input.clear()

    print(country_population)
    result_df = pd.DataFrame(country_population, columns=["pop"])
    result_df.to_csv("country_population.csv")


df = pd.read_csv("Country-data.csv")
fetch_country_population(np.array(df["country"]), path)
