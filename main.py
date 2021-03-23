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

your_list = ['fat_100g','energy_100g', 'sugars_100g', 'fiber_100g', 'proteins_100g', 'sodium_100g', 'saturated-fat_100g']
for i in your_list:
    data.loc[data[i].isnull(),i]=0

data = data[data["nutrition_grade_fr"].isnull() == False]

sugars_outliers = data.loc[data["sugars_100g"] > 100 ]
sugars_outliers1 = data.loc[data["sugars_100g"] < 0 ]
fiber_outliers = data.loc[data["fiber_100g"] > 100 ]
fiber_outliers1 = data.loc[data["fiber_100g"] < 0 ]
proteins_outliers = data.loc[data["proteins_100g"] > 100 ]
proteins_outliers1 = data.loc[data["proteins_100g"] < 0 ]
sodium_outliers = data.loc[data["sodium_100g"] > 100 ]
sodium_outliers1 = data.loc[data["sodium_100g"] < 0 ]
fat_outliers = data.loc[data["fat_100g"] > 100 ]
fat_outliers1 = data.loc[data["fat_100g"] < 0 ]

data = data.drop(sugars_outliers1.index, axis=0)
data = data.drop(sugars_outliers.index, axis=0)
data = data.drop(proteins_outliers.index, axis=0)
data = data.drop(fiber_outliers.index, axis=0)






data_clean.shape

data_clean.to_csv('/home/apprenant/Desktop/FARIZD/FOOD/Data/intermediate.csv')