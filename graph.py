import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
print ("Setup Complete")

file_path = "/home/apprenant/Desktop/FARIZD/FOOD/Data/intermediate.csv"
df = pd.read_csv(file_path)

profile = ProfileReport(df, title = 'Pandas Profiling Report')

profile.to_file("your_report.html")