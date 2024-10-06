import pandas as pd


def load_data():
    product_df = pd.read_csv('data/product.csv', delimiter=',', encoding='ISO-8859-1')  
    package_df = pd.read_csv('data/package.csv', delimiter=',', encoding='ISO-8859-1')  
    
    return product_df, package_df

product_df, package_df = load_data()

print("Product DataFrame Columns:", product_df.columns)
print("Package DataFrame Columns:", package_df.columns)

def clean_data(product_df, package_df):
   
    package_df = package_df.fillna(method='ffill')
    
   
    product_columns = product_df.columns.str.strip().str.upper()  
    package_columns = package_df.columns.str.strip().str.upper()

    if 'STARTMARKETINGDATE' not in product_columns or 'ENDMARKETINGDATE' not in product_columns:
        print("Warning: 'STARTMARKETINGDATE' or 'ENDMARKETINGDATE' not found in product data. Please check column names.")
    
    if 'STARTMARKETINGDATE' not in package_columns or 'ENDMARKETINGDATE' not in package_columns:
        print("Warning: 'STARTMARKETINGDATE' or 'ENDMARKETINGDATE' not found in package data. Please check column names.")
    
    
    product_df.columns = product_columns
    package_df.columns = package_columns

    
    product_df['STARTMARKETINGDATE'] = pd.to_datetime(product_df['STARTMARKETINGDATE'], format='%Y%m%d', errors='coerce')
    product_df['ENDMARKETINGDATE'] = pd.to_datetime(product_df['ENDMARKETINGDATE'], format='%Y%m%d', errors='coerce')

    package_df['STARTMARKETINGDATE'] = pd.to_datetime(package_df['STARTMARKETINGDATE'], format='%Y%m%d', errors='coerce')   
    package_df['ENDMARKETINGDATE'] = pd.to_datetime(package_df['ENDMARKETINGDATE'], format='%Y%m%d', errors='coerce')
    
    return product_df, package_df


clean_product_df, clean_package_df = clean_data(product_df, package_df)


if __name__ == "__main__":
    product_df, package_df = load_data()
    clean_product_df, clean_package_df = clean_data(product_df, package_df)
    clean_product_df.to_csv('data/clean_product1.csv', index=False)
    clean_package_df.to_csv('data/clean_package1.csv', index=False)
