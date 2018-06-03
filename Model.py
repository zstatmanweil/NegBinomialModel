import statsmodels.api as sm

class Neg_Bin_Model(object):
    
    def __init__(self, data, violation_type):
        self.data = data
        self.violation_type = violation_type
            
    def run(self):
        #define the target and predictors 
        target = self.data[self.violation_type]
        predictors = self.data.loc[:,("Percent_Below_Poverty_Line", 
                                      "Percent_Minority", 
                                      "Rural", 
                                      "Private",
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