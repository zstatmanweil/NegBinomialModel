import pandas as pd
import numpy as np

class SummaryStats(object):
    
    def __init__(self, df, continuous_column_names, cat_column_names):
        self.df = df
        self.continuous_column_names = continuous_column_names
        self.cat_column_names = cat_column_names
        
    
    def get_mean(self):
        return self.df.loc[:,self.continuous_column_names].mean()
    
    def get_std(self):
        return self.df.loc[:,self.continuous_column_names].std()
        
    def get_min(self):
        return self.df.loc[:,self.continuous_column_names].min()
    
    def get_max(self):
        return self.df.loc[:,self.continuous_column_names].max()
    
    def cont_summary_table(self):
        sum_table = pd.DataFrame(index=self.continuous_column_names)
        sum_table['Minimum'] = self.get_min()
        sum_table['Maximum'] = self.get_max()
        sum_table['Mean'] = self.get_mean()
        sum_table['SD'] = self.get_std()
        return sum_table

    def count_table(self):
        true_values = []
        false_values = []
        
        for name in self.cat_column_names:
            true_count = self.df[self.df[name]==1].loc[:,name].count()
            false_count = self.df[self.df[name]==0].loc[:,name].count()
            true_values.append(true_count)
            false_values.append(false_count)
        
        counts = {"No": false_values, "Yes": true_values}
        sum_table = pd.DataFrame(counts, index=self.cat_column_names)
        return sum_table  
