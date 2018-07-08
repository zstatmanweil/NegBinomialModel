import statsmodels.api as sm
import pandas as pd
from Variables import Variables
from Model import Neg_Bin_Model
from SummaryStats import Summary_Stats
import os

wd = os.chdir("C:\Users\zstat\Box Sync\WaterContamination\Data Analysis\Processed\Python")

#Select the data set
#data = 'Dasymetric_Data.csv'
#data = 'ArealWeighting_Data.csv'
data = 'Interpolation_data.csv'

#read relevant csv 
df = pd.read_csv(data)

#isolate only connections less than 200
#df = df[df["Service_Connections_Count"] >= 200]

#add dummy variables
new_df = Variables(df)
new_df.add_all_variables()
complete_df = new_df.df

#analyze data
model = Neg_Bin_Model(complete_df, "All_Violations")

model.summarize()
#model.get_mle_retvals()

#get summary stats
continuous_columns = ("Percent_Below_Poverty_Line", "Percent_Minority")
cat_columns = ("Rural", "Public","ConnectionsLess200", "GroundwaterOrCombined")
test = Summary_Stats(complete_df, continuous_columns, cat_columns)
print test.get_cont_summary_table(), "\n"
print test.get_count_table()