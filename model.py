import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd

class Neg_Bin_Model(object):
    
    def __init__(self, df, violation_type, data):
        self.data = data
        self.df = df
        self.violation_type = violation_type
        self.model_fit = None

        #define the target and predictors 
        self.target = self.df[self.violation_type]
        self.predictors = self.df.loc[:,("Percent_Below_Poverty_Line", 
                                      "Percent_Minority", 
                                      "Rural", 
                                      "Public",
                                      "ConnectionsLess200", 
                                      "GroundwaterOrCombined"
                                      )]
    def fit(self):
        if not self.model_fit:
            self.model_fit = self.run().fit(maxiter=100)
        return self.model_fit
         
    def run(self):
        X = sm.add_constant(self.predictors)
        y = self.target
        
# =============================================================================
#         There are two ways to run the negative binomial regression using 
#         statsmodel. One way provides a value for alpha (dispersion paramater), 
#         and one does not but provides an easy way to get residuals. Thus, I 
#         ran the way that provides the alpha for each dataset, recorded alpha below, 
#         and reran with the method (GLM) that provides an easy way to analyze residuals. .
# =============================================================================
        alpha_data = {"All_Violations": [2.0174, 2.0165, 1.9930, 1.9619],
                      "Violations_Yes_HealthBased": [3.8892, 3.8431, 3.8556, 3.8696]}
        alpha_df = pd.DataFrame(alpha_data, index=['Dasymetric_Data.csv', 'ArealWeighting_Data.csv', 'Interpolation_data.csv', 'County_Data.csv'])
        a = alpha_df.loc[self.data, self.violation_type]
         
        model = sm.GLM(y,X,family=sm.families.NegativeBinomial(alpha=a))
        
        # Method which provides alpha: 
        #model = sm.NegativeBinomial(y,X)
        return model      
    
    def summarize(self):        
        print(self.fit().summary2())
        
    def get_mle_retvals(self):
        print(self.fit().mle_retvals)
        
    def get_pearson(self):
        print(self.fit().pearson_chi2)
        
    def get_predictions(self):
        params = self.fit().params
        self.df["Predictions"] = self.run().predict(params)
               
    def get_residuals(self):
        self.df["Residuals"] = self.fit().resid_response
        
    def get_pearson_residuals(self):
        self.df["Std_Pearson_Residuals"] = self.fit().resid_pearson
        
    def get_deviance_residuals(self):
        self.df["Std_Deviance_Residuals"] = self.fit().resid_deviance
        
