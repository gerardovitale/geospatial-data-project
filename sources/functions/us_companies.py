import search_place.properties.client as mongo
import pandas as pd
import numpy as np

def us_companies():
    filt = {
        'offices.country_code':'USA'
    }
    project = {
        '_id':0,
        'name':1,
        'category_code':1,
        'number_of_employees':1,
        'founded_year':1,
        'total_money_raised':1,
        'offices':1
    }
    usa_co = mongo.db.companies_unwinded.find(filt, project)
    df_usa_co = pd.json_normalize(usa_co)
    df_usa_co['total_money_raised'] = df_usa_co['total_money_raised'].apply(lambda x: x[1:-1].replace('$', '').replace('€', ''))
    df_usa_co['total_money_raised'] = df_usa_co['total_money_raised'].apply(pd.to_numeric)
    df_usa_co.to_csv('../../data/us-companies.csv')

us_companies()