# Overview
## Negative Binomial Regression Model
This is the code for the negative binomial regression model I developed for my thesis on disparities in Pennsylvania community water systems' compliance with the Safe Drinking Water Act (SDWA). My thesis compared the demographics of water systems with the number of SDWA violations received by those water systems. I used these scripts to explore and analyze the SDWA violation data. The negative binomial regression model helped me determine which variables have a statistically significant relationship with those violations.

## Installing Dependencies
`pip install -r requirements.txt`

## Organization
- I utilized [`main.py`](https://github.com/zstatmanweil/NegBinomialModel/blob/master/Main.py) to select my dataset, run the model, and get other key information to help me analyze my data and results. I was able to easily toggle between my datasets and make tweaks to my method without rewriting much code. 
- [`model.py`](https://github.com/zstatmanweil/NegBinomialModel/blob/master/Model.py) contains a Model class with functions related to running and analyzing the model (e.g., get_residuals()).
- [`variables.py`](https://github.com/zstatmanweil/NegBinomialModel/blob/master/Variables.py) contains a Variable class with functions to add variables (e.g., dummy variables). 
- [`summaryStats.py`](https://github.com/zstatmanweil/NegBinomialModel/blob/master/SummaryStats.py) contains a Summary class with functions to organize and summarize variables. 

## What Next?
I am currently conducting the same type of spatial environmental justice analysis I did for my thesis on disparities in compliance with the Safe Drinking Water Act (SDWA), but this time entirely in Python rather than with desktop geospatial software (e.g., ArcGIS). The results will be displayed in an interactive web application. Additionally, my thesis focused on Pennsylvania, but this project will focus on New Jersey so I can compare my results. This project will give me the opportunity to use geospatial Python libraries (e.g., geopandas, rasterio), grow my web development skills, and create a beautiful and useful web map where the user can explore drinking water quality and environmental justice concerns. For more information on this project, see this repository: [EJ-analysis-map](https://github.com/zstatmanweil/EJ-analysis-map).
