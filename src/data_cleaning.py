import pandas as pd

# Function to load the data with error handling for encoding issues
def load_data():
    try:
        # Try loading with UTF-8 encoding
        product_df = pd.read_csv('data/product.csv', delimiter=',', encoding='utf-8')  # changed delimiter to ','
        package_df = pd.read_csv('data/package.csv', delimiter=',', encoding='utf-8')  # changed delimiter to ','
    except UnicodeDecodeError:
        # Fallback to ISO-8859-1 encoding if UTF-8 fails
        print("UTF-8 decoding failed, trying ISO-8859-1.")
        product_df = pd.read_csv('data/product.csv', delimiter=',', encoding='ISO-8859-1')  # changed delimiter to ','
        package_df = pd.read_csv('data/package.csv', delimiter=',', encoding='ISO-8859-1')  # changed delimiter to ','
    
    return product_df, package_df

# Call the load_data function
product_df, package_df = load_data()

# Print the column names to check for discrepancies
print("Product DataFrame Columns:", product_df.columns)
print("Package DataFrame Columns:", package_df.columns)

# Function to clean the data
def clean_data(product_df, package_df):
    # Forward fill missing values for the package dataframe
    package_df = package_df.fillna(method='ffill')
    
    # Check if STARTMARKETINGDATE and ENDMARKETINGDATE exist in both dataframes
    product_columns = product_df.columns.str.strip().str.upper()  # Normalize column names
    package_columns = package_df.columns.str.strip().str.upper()

    if 'STARTMARKETINGDATE' not in product_columns or 'ENDMARKETINGDATE' not in product_columns:
        print("Warning: 'STARTMARKETINGDATE' or 'ENDMARKETINGDATE' not found in product data. Please check column names.")
    
    if 'STARTMARKETINGDATE' not in package_columns or 'ENDMARKETINGDATE' not in package_columns:
        print("Warning: 'STARTMARKETINGDATE' or 'ENDMARKETINGDATE' not found in package data. Please check column names.")
    
    # Rename columns to ensure consistency (strip spaces and convert to uppercase)
    product_df.columns = product_columns
    package_df.columns = package_columns

    # If the dates follow a specific format like YYYYMMDD, you can define it explicitly
    product_df['STARTMARKETINGDATE'] = pd.to_datetime(product_df['STARTMARKETINGDATE'], format='%Y%m%d', errors='coerce')
    product_df['ENDMARKETINGDATE'] = pd.to_datetime(product_df['ENDMARKETINGDATE'], format='%Y%m%d', errors='coerce')

    package_df['STARTMARKETINGDATE'] = pd.to_datetime(package_df['STARTMARKETINGDATE'], format='%Y%m%d', errors='coerce')   
    package_df['ENDMARKETINGDATE'] = pd.to_datetime(package_df['ENDMARKETINGDATE'], format='%Y%m%d', errors='coerce')
    
    return product_df, package_df

# Assuming data is loaded
clean_product_df, clean_package_df = clean_data(product_df, package_df)

# Main block to save cleaned data
if __name__ == "__main__":
    product_df, package_df = load_data()
    clean_product_df, clean_package_df = clean_data(product_df, package_df)
    clean_product_df.to_csv('data/clean_product1.csv', index=False)
    clean_package_df.to_csv('data/clean_package1.csv', index=False)
