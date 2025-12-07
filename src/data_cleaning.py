"""
Data Cleaning Script for Sales Dataset
ISM 2411 Portfolio Project

This script takes a messy sales CSV file and cleans it by:
- Standardizing column names
- Removing whitespace from text fields
- Handling missing values
- Removing invalid data entries

Author: Jose Guilherme Brol Leal 
Date: December 6, 2025
"""

import pandas as pd


def load_data(file_path: str):
    """
    Load the raw sales data from a CSV file.
    
    Args:
        file_path: Path to the raw CSV file
        
    Returns:
        DataFrame containing the raw sales data
    """
    df = pd.read_csv(file_path)
    print(f"Loaded {len(df)} rows from {file_path}")
    print(f"Original columns: {list(df.columns)}")
    return df


def clean_column_names(df):
    """
    Standardize column names to lowercase with underscores.
    
    This makes the data easier to work with in Python by following
    standard naming conventions. Inconsistent column names (with spaces
    and mixed capitalization) can cause errors when trying to access data.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with cleaned column names
    """
    # Strip whitespace from column names first, then standardize
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    print(f"Cleaned column names: {list(df.columns)}")
    return df


def strip_whitespace(df):
    """
    Remove leading and trailing whitespace from text columns.
    
    Extra whitespace can cause issues with data analysis and matching.
    For example, " Laptop" and "Laptop" would be treated as different
    products even though they're the same.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with whitespace removed from text fields
    """
    # Strip whitespace from all object (string) columns
    for col in df.select_dtypes(include=['object']).columns:
        # First remove any quotes
        df[col] = df[col].str.replace('"', '', regex=False)
        # Then strip leading/trailing whitespace
        df[col] = df[col].str.strip()
        # Standardize multiple spaces to single space
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True)
    print("Stripped whitespace and cleaned text columns")
    return df


def standardize_text_fields(df):
    """
    Standardize text formatting in product names and categories.
    
    Consistent capitalization makes the data look more professional
    and helps with grouping and analysis. For example, "electronics"
    and "Electronics" should be treated as the same category.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with standardized text formatting
    """
    # Capitalize category names (e.g., "electronics" -> "Electronics")
    if 'category' in df.columns:
        df['category'] = df['category'].str.title()
    
    # Capitalize product names for consistency
    if 'prodname' in df.columns:
        df['prodname'] = df['prodname'].str.title()
    
    print("Standardized text formatting (capitalization)")
    return df


def convert_data_types(df):
    """
    Convert columns to appropriate data types.
    
    The CSV file stores everything as strings, but price and qty should
    be numeric for calculations. This function converts them and handles
    any values that can't be converted (setting them to NaN).
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with correct data types
    """
    # Convert price and qty to numeric, coercing errors to NaN
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')
    print("Converted price and qty to numeric types")
    return df


def handle_missing_values(df):
    """
    Handle missing values in the dataset.
    
    Missing prices and quantities make records unusable for analysis.
    We drop these rows because we can't accurately calculate revenue
    or perform sales analysis without complete information.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with missing values handled
    """
    initial_rows = len(df)
    
    # Drop rows where price or qty is missing (NaN)
    df = df.dropna(subset=['price', 'qty'])
    
    rows_dropped = initial_rows - len(df)
    print(f"Dropped {rows_dropped} rows with missing price or qty")
    return df


def remove_invalid_rows(df):
    """
    Remove rows with invalid data values.
    
    Negative prices and quantities are data entry errors and don't
    represent real transactions. Zero quantities are also invalid as
    they indicate no actual sale occurred. We remove these to ensure 
    data quality and prevent incorrect calculations in analysis.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with invalid rows removed
    """
    initial_rows = len(df)
    
    # Remove rows with negative or zero price or quantity
    df = df[(df['price'] > 0) & (df['qty'] > 0)]
    
    rows_removed = initial_rows - len(df)
    print(f"Removed {rows_removed} rows with invalid values (negative or zero)")
    return df


def add_revenue_column(df):
    """
    Calculate revenue for each transaction.
    
    Revenue (price * quantity) is a key metric for sales analysis.
    Adding this column makes it easier to analyze sales performance
    and identify top-performing products or categories.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with revenue column added
    """
    df['revenue'] = (df['price'] * df['qty']).round(2)
    print("Added revenue column")
    return df


def remove_duplicates(df):
    """
    Remove duplicate rows from the dataset.
    
    Duplicate entries can skew analysis and inflate sales numbers.
    We identify duplicates based on product name, price, and quantity,
    keeping the first occurrence and removing subsequent duplicates.
    We ignore category and date differences to catch potential 
    miscategorized duplicates.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with duplicates removed
    """
    initial_rows = len(df)
    # Remove duplicates based on key columns (ignore category and date for duplicate detection)
    df = df.drop_duplicates(subset=['prodname', 'price', 'qty'], keep='first')
    rows_removed = initial_rows - len(df)
    print(f"Removed {rows_removed} duplicate rows")
    return df


if __name__ == "__main__":
    # File paths
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"
    
    # Run the cleaning pipeline
    print("\n=== Starting Data Cleaning Pipeline ===\n")
    
    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = strip_whitespace(df_clean)
    df_clean = standardize_text_fields(df_clean)
    df_clean = convert_data_types(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean = remove_duplicates(df_clean)
    df_clean = add_revenue_column(df_clean)
    
    # Save cleaned data
    df_clean.to_csv(cleaned_path, index=False)
    print(f"\n=== Cleaning Complete ===")
    print(f"Cleaned data saved to {cleaned_path}")
    print(f"\nFinal dataset: {len(df_clean)} rows, {len(df_clean.columns)} columns")
    print("\nFirst few rows:")
    print(df_clean.head())
    print("\nData types:")
    print(df_clean.dtypes)
    print("\nBasic statistics:")
    print(df_clean[['price', 'qty', 'revenue']].describe())