# Pharma Analysis Project

## Overview

This project performs an analysis on pharmaceutical data using the `product.csv` file to examine trends in drug types and pharmaceutical classes. It includes functions to visualize the most common drug types and pharmaceutical classes, as well as trends over time for drug types.

The analysis also includes data cleaning functions to ensure that the columns are standardized and date formats are properly handled.

## Prerequisites

To run this project, you'll need to have the following libraries installed:

- `pandas`
- `seaborn`
- `matplotlib`
- `statsmodels`

You can install the required packages using the following commands:

```bash
pip install pandas seaborn matplotlib statsmodels
```

## Files

- **`data/clean_product.csv`**: The cleaned version of the `product.csv` dataset.
- **`data/clean_package.csv`**: The cleaned version of the `package.csv` dataset.

## Code Structure

### 1. **`data_analysis.py`**
This script performs the following analyses:

- **Drug Type Analysis**: 
  - Plots the top 10 most common drug types.
  - Visualizes the distribution of the top 5 drug types as a pie chart.

- **Pharmaceutical Classes Analysis**:
  - Plots the top 10 most common pharmaceutical classes.
  - Visualizes the distribution of the top 5 pharmaceutical classes as a pie chart.

- **Drug Type Trends Over Time**:
  - Groups the data by year and month to visualize the trends of different drug types.

#### Key Functions:

- `load_data(filepath)`: Loads the product dataset from the provided file path.
- `analyze_drug_types(product_df)`: Analyzes the frequency distribution of drug types and creates visualizations.
- `analyze_pharmaceutical_classes(product_df)`: Analyzes the frequency distribution of pharmaceutical classes and creates visualizations.
- `main()`: Main function to load the dataset and perform the analyses.

### 2. **`data_cleaning.py`**
This script focuses on cleaning the `product.csv` and `package.csv` datasets.

#### Key Functions:

- `load_data()`: Loads the `product.csv` and `package.csv` files.
- `clean_data(product_df, package_df)`: Cleans the data by handling missing values, converting date columns to the appropriate format, and ensuring the consistency of column names.

## How to Use

### Running the Analysis

1. **Clone the repository** and navigate to the project directory.

2. **Run the data cleaning script**:
   ```bash
   python data_cleaning.py
   ```
   This will clean the `product.csv` and `package.csv` datasets and save them as `clean_product.csv` and `clean_package.csv` in the `data/` folder.

3. **Run the data analysis script**:
   ```bash
   python data_analysis.py
   ```
   This will generate various plots for analyzing drug types and pharmaceutical classes.

### Output

The analysis will output the following visualizations:
- Top 10 most common drug types (bar plot).
- Top 5 drug types distribution (pie chart).
- Top 10 most common pharmaceutical classes (bar plot).
- Top 5 pharmaceutical classes distribution (pie chart).
- Trends in drug types over time (line plot).

