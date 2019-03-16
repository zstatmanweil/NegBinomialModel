import pandas as pd
import numpy as np

class Variables(object):
    
    def __init__(self, df):
        self.df = df
        
    def add_all_variables(self):
        self.rural_urban()
        self.owner_type_public()
        self.few_sewer_connections()
        self.groundwater_source()

    # Get dummy variables for rural vs urban and owner type and 
    # concactenate to original table 
    def rural_urban(self):
        dummyUR = pd.get_dummies(self.df['Urban_Rural'])
        self.df = pd.concat([self.df, dummyUR], axis=1)
   
    # Create a private vs public variable
    def owner_type_public(self):
        self.df["Public"] = np.where(
                (np.logical_or(self.df["Owner_Type"]=="Private", self.df["Owner_Type"]=="Public/Private")), 0, 1)
        
    # Create a column identifying all public water systems with service connections less than 200
    def few_sewer_connections(self):
        self.df["ConnectionsLess200"] = np.where(
                self.df["Service_Connections_Count"] <= 200, 1, 0)
        
    # Create a column identifying all public water systems with groundwater sources
    def groundwater_source(self):
        self.df["GroundwaterOrCombined"] = np.where(
                (np.logical_or(self.df["Primary_Source"] ==
                "Surface water purchased", self.df["Primary_Source"] =="Surface water")), 0, 1)
