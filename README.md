# Overview
## Negative Binomial Regression Model
This is the code for the negative binomial regression model I developed for my thesis on disparities in community water systems' compliance with the Safe Drinking Water Act (SDWA). My thesis compared the demographics of water systems with the number of SDWA violations received by those water systems. I used these scripts to explore and analyze the SDWA violation data. The negative binomial regression model helped me determine which variables have a statistically significant relationship with those violations.

## Organization
- I utilized [`/Main.py`](https://github.com/zstatmanweil/NegBinomialModel/blob/master/Main.py) to select my dataset, run the model, and get other key information to help me analyze my data and results. I was able to easily toggle between my datasets and make tweaks to my method without rewriting much code. 
- [`/Model.py`](https://github.com/zstatmanweil/NegBinomialModel/blob/master/Model.py) contains a Model class with functions related to running and analyzing the model (e.g., get_residuals()).
- [`/Variables.py`](https://github.com/zstatmanweil/NegBinomialModel/blob/master/Variables.py) contains a Variable class with functions to add variables (e.g., dummy variables). 
- [`/SummaryStates.py`](https://github.com/zstatmanweil/NegBinomialModel/blob/master/SummaryStates.py) contains a Summary class with functions to organize and summarize variables. 

