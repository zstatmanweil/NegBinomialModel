import pandas as pd
from Variables import Variables
from Model import Neg_Bin_Model
from SummaryStats import Summary_Stats
import os
import matplotlib.pyplot as plt

wd = os.chdir(r"C:\Users\zstat\Box Sync\WaterContamination\Data Analysis\Processed\Python")

#Select the data set
#data = 'Dasymetric_Data.csv'
#data = 'ArealWeighting_Data.csv'
#data = 'Interpolation_data.csv'
data = 'County_Data.csv'

#read relevant csv  
df = pd.read_csv(data)

#select violation data of interest
#vio_data = "All_Violations"
vio_data = "Violations_Yes_HealthBased"

#add dummy variables
new_df = Variables(df)
new_df.add_all_variables()
complete_df = new_df.df

#analyze data
model = Neg_Bin_Model(complete_df, vio_data, data)
model.summarize()
print "pearson chi2:", model.get_pearson()
#model.get_mle_retvals()

#get predictions
model.get_predictions()

#get residuals
model.get_pearson_residuals()
model.get_deviance_residuals()
model.get_residuals()

#get summary stats
continuous_columns = ("Percent_Below_Poverty_Line", "Percent_Minority")
cat_columns = ("Rural", "Public","ConnectionsLess200", "GroundwaterOrCombined")
summary = Summary_Stats(complete_df, continuous_columns, cat_columns)
print summary.get_cont_summary_table(), "\n"
print summary.get_count_table()

#explore residuals
pd.set_option('max_columns', 7)
print model.df[["Predictions","Std_Pearson_Residuals","Std_Deviance_Residuals", "Residuals"]].head(5)

#create plot of residuals
# =============================================================================
# plt.scatter(model.df["Predictions"], model.df["Std_Deviance_Residuals"], s=5, color="black")
# plt.xlabel("Predicted Value of Mean Response")
# plt.ylabel("Standardized Deviance Residuals")
# #plt.xlim([0,5])
# #plt.ylim([-3, 6])
# =============================================================================

#export DataFrame to csv
model.df.to_csv("C:\Users\zstat\Box Sync\WaterContamination\Data Analysis"\
                "\Processed\Python\NegBinomialModel\Export"\
                "\\" + data[0:-9] + "_" + vio_data + ".csv")