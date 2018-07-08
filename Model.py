import statsmodels.api as sm

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

        model = sm.NegativeBinomial(y,X)
        res = model.fit()
        
        return res
    
    def summarize(self):        
        print self.run().summary2()
        
    def get_mle_retvals(self):
        print self.run().mle_retvals