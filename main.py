import pandas as pd
import csv
import missingno as msno 
import re
  


data_c = pd.read_csv('/home/apprenant/Desktop/FARIZD/FOOD/Data/en.openfoodfacts.org.products.tsv', sep='\t')

data_clean = data_c.sample(n=30000)


data_clean = data_clean[['countries', 'categories', 'product_name', 'energy_100g', 'sugars_100g', 'fiber_100g', 'proteins_100g', 'sodium_100g', 'saturated-fat_100g', 'nutrition-score-fr_100g', 'nutrition_grade_fr','fat_100g','additives_n','additives','additives_tags']]

data_clean["countries"] = data_clean["countries"].apply(
    lambda x: "France" if re.match(r".*(fr).*", str(x), re.IGNORECASE) else x )


data_clean = data_clean.loc[data_clean.countries == 'France']


data_clean = data_clean[data_clean["product_name"].isnull() == False]


data_clean = data_clean.dropna(subset=['fat_100g','energy_100g', 'sugars_100g', 'fiber_100g', 'proteins_100g', 'sodium_100g', 'saturated-fat_100g'],how ='all')


data_clean.shape

data_clean.to_csv('/home/apprenant/Desktop/FARIZD/FOOD/Data/intermediate.csv')