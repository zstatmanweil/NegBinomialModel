import pandas as pd
import numpy as np

class Variables(object):
    
    def __init__(self, data):
        self.data = data
        
    def add_all_variables(self):
        self.rural_urban()
        self.owner_type_private()
        self.few_sewer_connections()
        self.groundwater_source()

    #get dummy variables for Rural vs Urban and Owner Type and 
    #concactenate to original table
    def rural_urban(self):
        dummyUR = pd.get_dummies(self.data['Urban_Rural'])
        self.data = pd.concat([self.data, dummyUR], axis=1)
   
    #create a Private vs Public Variable
    def owner_type_private(self):
        self.data["Private"] = np.where(
                (np.logical_or(self.data["Owner_Type"]=="Private", self.data["Owner_Type"]=="Public/Private")), 1, 0)
        
    #create a column identifying all PWS with service connections less than 200
    def few_sewer_connections(self):
        self.data["ConnectionsLess200"] = np.where(
                self.data["Service_Connections_Count"] <= 200, 1, 0)
        
        #create a golumn identifying all PWS with groundwater sources
    def groundwater_source(self):
        self.data["GroundwaterOrCombined"] = np.where(
                (np.logical_or(self.data["Primary_Source"] ==
                "Surface water purchased", self.data["Primary_Source"] =="Surface water")), 0, 1)