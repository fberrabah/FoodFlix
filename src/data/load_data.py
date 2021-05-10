# Importing the libraries
import sys
sys.path.insert(0,"/home/apprenant/Desktop/FARIZD/FOOD/")

import pandas as pd
from IPython.display import Image, HTML
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS



# Importing the dataset
listings = pd.read_csv('/home/apprenant/Desktop/FARIZD/FOOD/Data/intermediate.csv')


listings.head(10)


#FillNa
listings['content'] = listings[['product_name']].astype(str).apply(lambda x: ' // '.join(x), axis = 1)
listings['content'].fillna('Null', inplace = True)


listings['product_name'] = listings['product_name'].astype('str')
name_corpus = ' '.join(listings['product_name'])


STOPWORDSFR = {'le', 'la', 'de', 'du', 'au', 'les', 'aux', 'null'}