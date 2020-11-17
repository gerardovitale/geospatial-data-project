import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

URL = 'https://thegedi.org/global-entrepreneurship-and-development-index/'

# def get_gei():
data_gei = requests.get(URL)
soup_gei = BeautifulSoup(data_gei.text)
gei_heads = soup_gei.select('th')
gei = soup_gei.select('td')

arr = np.empty((15,4), dtype='S25')
i, j, k = 0, 0, 0
while i < len(arr):
    arr[i,j] = gei[k].text
    k += 1
    j += 1
    if j > 3:
        j = 0
        i += 1

df_gei = pd.DataFrame(arr, columns=['rank', 'country', 'GDP', 'GEI'])
df_gei[['rank', 'GDP', 'GEI']] = df_gei[['rank', 'GDP', 'GEI']].apply(pd.to_numeric)
df_gei['country'] = df_gei['country'].apply(lambda x: x.decode('utf-8'))
df_gei.set_index('rank')
# print(df_gei)
df_gei.to_csv('../../data/global-entrepreneurship-index.csv')