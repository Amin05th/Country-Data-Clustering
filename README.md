# Country-Data-Clustering: Project Overview

- Created an app that clusters countrys based on several features
- Downloaded Kaggle Dataset Unsupervised Learning on Country Data
- Created preprocessing classes for Removing Countryname, Adding Feature (population) scraped using selenuium and python, Imputed Values
- Optimized KMeans, MiniBatchKMeans, SpectralClustering and AgglomerativeClustering
- Build a client facing API using flask
- Created User Interface using flask, html and css

## Code and Resources Used

- ** Python Version: ** 3.10
- ** Packages: ** pandas, numpy, sklearn, matplotlib, seaborn, flask, mpl_toolkits, mplcursors, flask_restx, flask_sqlalchemy, sqlalchemy
- ** Kaggle Dataset **: [https://www.kaggle.com/datasets/rohan0301/unsupervised-learning-on-country-data](https://www.kaggle.com/datasets/rohan0301/unsupervised-learning-on-country-data)
- ** Scraping Resource: ** https://www.worldometers.info/world-population

## Downloaded Dataset

With this downloaded I got following features:

- country
- child_mort
- exports
- health
- imports
- income
- inflation
- life_expec
- total_fer
- gdpp
- pop


## Web Scraping

In order to get the population feature for the clustering algorithms I wrote an app using selenium and python to scrape from Worldometer
