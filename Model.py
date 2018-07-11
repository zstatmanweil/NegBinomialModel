import statsmodels.api as sm
import numpy as np

class Neg_Bin_Model(object):
    
    def __init__(self, df, violation_type):
        self.df = df
        self.violation_type = violation_type
            
    def run(self):
        #define the target and predictors 
        target = self.df[self.violation_type]
        predictors = self.df.loc[:,("Percent_Below_Poverty_Line", 
                                      "Percent_Minority", 
                                      "Rural", 
                                      "Public",
                                      "ConnectionsLess200", 
                                      "GroundwaterOrCombined"
                                      )]
        
        X = sm.add_constant(predictors)
        y = target
        #alpha=2.0174 (this is alpha in R)
        model = sm.GLM(y,X,family=sm.families.NegativeBinomial())
        #alternative: 
        #model = sm.NegativeBinomial(y,X)
        return model
    
    #def get_alpha():
    
    def summarize(self):        
        print self.run().fit().summary2()
        
    def get_mle_retvals(self):
        print self.run().fit().mle_retvals
        
    def get_predictions(self):
        self.df["Predictions"] = self.run().predict(self.run().fit().params)
               
    def get_residuals(self):
        self.df["Residuals"] = self.run().fit().resid_response
        
    def get_pearson_residuals(self):
        self.df["Std_Pearson_Residuals"] = self.run().fit().resid_pearson
        
    def get_deviance_residuals(self):
        self.df["Std_Deviance_Residuals"] = self.run().fit().resid_deviance