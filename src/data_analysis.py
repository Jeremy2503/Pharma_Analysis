# data_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load the dataset
def load_data(filepath):
    """Loads the product dataset from the provided file path."""
    return pd.read_csv(filepath)

# Function to analyze drug types
def analyze_drug_types(product_df):
    """Analyzes the frequency distribution of drug types and plots visualizations."""
    # Frequency of Drug Types (PRODUCTTYPENAME)
    drug_type_counts = product_df['PRODUCTTYPENAME'].value_counts()
    
    # Bar plot for the top 10 drug types
    plt.figure(figsize=(10,6))
    sns.barplot(x=drug_type_counts.head(10).index, y=drug_type_counts.head(10).values, palette='viridis')
    plt.title('Top 10 Most Common Drug Types', fontsize=16)
    plt.xlabel('Drug Type', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Pie chart for top 5 drug types
    plt.figure(figsize=(7,7))
    plt.pie(drug_type_counts.head(5), labels=drug_type_counts.head(5).index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2'))
    plt.title('Top 5 Drug Types Distribution', fontsize=14)
    plt.show()

# Function to analyze pharmaceutical classes
def analyze_pharmaceutical_classes(product_df):
    """Analyzes the frequency distribution of pharmaceutical classes and plots visualizations."""
    # Frequency of Pharmaceutical Classes (PHARM_CLASSES)
    pharm_class_counts = product_df['PHARM_CLASSES'].value_counts()
    
    # Bar plot for the top 10 pharmaceutical classes
    plt.figure(figsize=(10,6))
    sns.barplot(x=pharm_class_counts.head(10).index, y=pharm_class_counts.head(10).values, palette='coolwarm')
    plt.title('Top 10 Most Common Pharmaceutical Classes', fontsize=16)
    plt.xlabel('Pharmaceutical Class', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Pie chart for top 5 pharmaceutical classes
    plt.figure(figsize=(7,7))
    plt.pie(pharm_class_counts.head(5), labels=pharm_class_counts.head(5).index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3'))
    plt.title('Top 5 Pharmaceutical Classes Distribution', fontsize=14)
    plt.show()

# Main function to run the analysis
def main():
    # Load the product dataset
    filepath = 'C:/Users/j7902/Desktop/Pharma_Analysis/data/clean_product.csv'
    product_df = load_data(filepath)
    
    # Display first few rows of the dataset
    print("First 5 rows of the dataset:")
    print(product_df.head())
    
    # Perform analysis on drug types
    print("\nAnalyzing Drug Types...")
    analyze_drug_types(product_df)
    
    # Perform analysis on pharmaceutical classes
    print("\nAnalyzing Pharmaceutical Classes...")
    analyze_pharmaceutical_classes(product_df)

# Entry point for the script
if __name__ == "__main__":
    main()
