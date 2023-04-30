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

In order to get the population feature for the clustering algorithms I wrote an app using selenium and python to scrape data from Worldometer

## Data Preprocessing

After Downloading and Scraping Data i preprocessed the data so that it was usable for our model. I made the following changes and created the following features:


- Removed country names
- Added population feature
- Imputed scraped Population data
- changed Country Names in order for the API to understand

## EDA

Created Plots to see better correlations between features and plotted §d graph to see how much country differentiate from each other.
![download](https://user-images.githubusercontent.com/86575364/235356223-393f7700-ef27-4c5c-85ef-1deebdbc0418.png)

## Model Building

I tried 4 different models and evaluated them using Scatter Plots. I chose Scatter plots for the reason that it is clear and when you cluster you have no labels to use metrics

I tried this following models:
- ** KMeans: ** Because of the normal data distribution
- ** MiniBatchKMeans: ** Thought it would be effective becouse of the mini batches
- ** SpectralClustering: ** Tried if dimention reduction is effective
- ** AgglomerativeClustering: ** Looked up other code and saw the algorith so I tried it


## Model evaluation

I plotted scatter plots to see how good the cluster clustered the data here are some pictures
![download](https://user-images.githubusercontent.com/86575364/235357109-769097dd-63ea-4a8f-bbc8-e1691f240cec.png)
![download](https://user-images.githubusercontent.com/86575364/235357104-90931f34-6d65-4e0f-8339-0c55f269a3a9.png)

## Productionization

In this step, I built a flask API endpoint that was hosted on a local webserer by following along with the TDS tutorial in the reference section above. The API endpoint show all values in JSON format and in single values in JSON format. For user to see the results visualy I created a User Interface using HTML and CSS.


