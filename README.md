Pharma Analysis Project
Overview
This project analyzes pharmaceutical data using the product.csv file. It visualizes trends in drug types and pharmaceutical classes and includes data cleaning functions to standardize columns and handle date formats.

Files
data/clean_product.csv: Cleaned product dataset.
data/clean_package.csv: Cleaned package dataset.
Code Structure
1. data_analysis.py
Performs the following analyses:

Drug Type Analysis: Plots the top 10 drug types and visualizes the top 5 as a pie chart.
Pharmaceutical Classes Analysis: Plots the top 10 pharmaceutical classes and shows the top 5 in a pie chart.
Drug Trends Over Time: Visualizes trends for different drug types.
2. data_cleaning.py
Cleans the product.csv and package.csv datasets by:

Handling missing values.
Converting dates into the correct format.
Standardizing column names.
How to Use
Clean the datasets: Run data_cleaning.py to generate clean_product.csv and clean_package.csv.

Analyze the data: Run data_analysis.py to generate various plots for drug type and pharmaceutical class trends.
