import pandas as pd
import csv
import missingno as msno 
  


data = pd.read_csv('/home/apprenant/Desktop/FARIZD/FOOD/Data/en.openfoodfacts.org.products.tsv', sep='\t')


print(data.head())
print(data.columns)
