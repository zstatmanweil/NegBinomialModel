import pandas as pd
import numpy as np

class Summary_Stats(object):
    
    def __init__(self, df, column_names):
        self.df = df
        self.column_names = column_names
        
    
    def get_mean(self):
        means = self.df.loc[:,self.column_names].mean()
        return means
    
    def get_std(self):
        stds = self.df.loc[:,self.column_names].std()
        return stds
        
    def get_min(self):
        mins = self.df.loc[:,self.column_names].min()
        return mins
    
    def get_max(self):
        maximums = means = self.df.loc[:,self.column_names].max()
        return maximums
    
    def get_summary_table(self):
        sum_table = pd.DataFrame(index=self.column_names)
        sum_table['Minimum'] = self.get_min()
        sum_table['Maximum'] = self.get_max()
        sum_table['Mean'] = self.get_mean()
        sum_table['SD'] = self.get_std()
        return sum_table

