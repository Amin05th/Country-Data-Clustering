from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import numpy as np

db = SQLAlchemy()

country_table = db.Table("country_clusters",
                         Column("id", Integer, primary_key=True),
                         Column("k_means", Integer),
                         Column("mini_batch_kmeans", Integer),
                         Column("spectralclustering", Integer),
                         Column("agglomerativeclustering", Integer),
                         Column("country", String))


def get_all_countries_arr():
    all_countries = db.session.query(country_table).all()
    return [country[5] for country in all_countries]



def get_all_countries():
    all_countries = db.session.query(country_table).all()
    return [
        {
            "id": country[0],
            "k_means": country[1],
            "mini_batch_kmeans": country[2],
            "spectralclustring": country[3],
            "agglomerativeclustering": country[4],
            "country": country[5],
        }
        for country in all_countries
    ]


def get_single_country(country_id):
    single_country = db.session.query(country_table).filter_by(id=country_id)[0]
    return {
        "id": single_country[0],
        "k_means": single_country[1],
        "mini_batch_kmeans": single_country[2],
        "spectralclustring": single_country[3],
        "agglomerativeclustering": single_country[4],
        "country": single_country[5],
    }

