import pandas as pd
import numpy as np

class Variables(object):
    
    def __init__(self, df):
        self.df = df
        
    def add_all_variables(self):
        self.rural_urban()
        self.owner_type_private()
        self.few_sewer_connections()
        self.groundwater_source()

    #get dummy variables for Rural vs Urban and Owner Type and 
    #concactenate to original table 
    def rural_urban(self):
        dummyUR = pd.get_dummies(self.df['Urban_Rural'])
        self.df = pd.concat([self.df, dummyUR], axis=1)
   
    #create a Private vs Public Variable
    def owner_type_private(self):
        self.df["Public"] = np.where(
                (np.logical_or(self.df["Owner_Type"]=="Private", self.df["Owner_Type"]=="Public/Private")), 0, 1)
        
    #create a column identifying all PWS with service connections less than 200
    def few_sewer_connections(self):
        self.df["ConnectionsLess200"] = np.where(
                self.df["Service_Connections_Count"] <= 200, 1, 0)
        
    #create a golumn identifying all PWS with groundwater sources
    def groundwater_source(self):
        self.df["GroundwaterOrCombined"] = np.where(
                (np.logical_or(self.df["Primary_Source"] ==
                "Surface water purchased", self.df["Primary_Source"] =="Surface water")), 0, 1)