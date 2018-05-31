import statsmodels.api as sm
import pandas as pd
from Variables import Variables
from Model import Neg_Bin_Model
import os

wd = os.chdir("C:\Users\zstat\Box Sync\WaterContamination\Data Analysis\Processed\Python")

#read relevant csv
df = pd.read_csv('Dasymetric_Data.csv')

#add dummy variables
new_data = Variables(df)
new_data.add_all_variables()

#analyze data
model = Neg_Bin_Model(new_data.data, "All_Violations")

model.summarize()
print new_data.data.loc[:,("Owner_Type","Private")].head(30)