import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd

class Neg_Bin_Model(object):
    
    def __init__(self, df, violation_type, data):
        self.data = data
        self.df = df
        self.violation_type = violation_type
        
        #define the target and predictors 
        self.target = self.df[self.violation_type]
        self.predictors = self.df.loc[:,("Percent_Below_Poverty_Line", 
                                      "Percent_Minority", 
                                      "Rural", 
                                      "Public",
                                      "ConnectionsLess200", 
                                      "GroundwaterOrCombined"
                                      )]
            
    def run(self):
        X = sm.add_constant(self.predictors)
        y = self.target
        
# =============================================================================
#         There are two ways to run the negative binomial regression using 
#         statsmodel. One way provides a value for alpha (dispersion paramater), 
#         and one does not but provides an easy way to get residuals. Thus, I 
#         ran the way that provides the alpha for each dataset and recorded each below.
# =============================================================================
        alpha_data = {"All_Violations": [2.0174, 2.0165, 1.9930],
                      "Violations_Yes_HealthBased": [3.8892, 3.8431, 3.8556]}
        alpha_df = pd.DataFrame(alpha_data, index=['Dasymetric_Data.csv', 'ArealWeighting_Data.csv', 'Interpolation_data.csv'])
        a = alpha_df.loc[self.data, self.violation_type]
        
        model = sm.GLM(y,X,family=sm.families.NegativeBinomial(alpha=a))
        
        #Method which provides alpha: 
        #model = sm.NegativeBinomial(y,X)
        return model      
    
    def summarize(self):        
        print self.run().fit(maxiter=100).summary2()
        
    def get_mle_retvals(self):
        print self.run().fit(maxiter=100).mle_retvals
        
    def get_pearson(self):
        print self.run().fit(maxiter=100).pearson_chi2
        
    def get_predictions(self):
        params = self.run().fit(maxiter=100).params
        self.df["Predictions"] = self.run().predict(params)
               
    def get_residuals(self):
        self.df["Residuals"] = self.run().fit(maxiter=100).resid_response
        
    def get_pearson_residuals(self):
        self.df["Std_Pearson_Residuals"] = self.run().fit(maxiter=100).resid_pearson
        
    def get_deviance_residuals(self):
        self.df["Std_Deviance_Residuals"] = self.run().fit(maxiter=100).resid_deviance
        
# =============================================================================
#     #to be deleted
#     def ct_response(self, row):
#         #Calculate response observation for Cameron-Trivedi dispersion test
#         y = row[self.violation_type]
#         m = row['vio_mu']
#         return (((y - m)**2) - y) / m
#     
#     def get_alpha(self):
#         X = sm.add_constant(self.predictors)
#         y = self.target
#         
#         ct_data = self.df.copy()
#         ct_data["vio_mu"] = sm.GLM(y,X,family=sm.families.Poisson()).fit().mu
#         ct_data["ct_resp"] = ct_data.apply(self.ct_response, axis=1)
#         # Linear regression of auxiliary formula
#         ct_results = smf.ols('ct_resp ~ vio_mu - 1', ct_data).fit()
#         # Construct confidence interval for alpha, the coefficient of vio_mu
#         alpha_ci95 = ct_results.conf_int(0.05).loc['vio_mu']
#         return ct_results.params[0] 
# =============================================================================
