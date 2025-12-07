# ism2411-data-cleaning-copilot
ISM 2411 Data Cleaning Project
A Python-based data cleaning project that processes messy sales data into a clean, analysis-ready format.

Project Description
This project demonstrates fundamental data cleaning techniques using Python and pandas. It takes a raw sales dataset with inconsistent formatting, missing values, and invalid entries, and transforms it into a clean CSV file ready for analysis.

Features
- Standardizes column names to lowercase with underscores
- Removes whitespace from text fields
- Handles missing values appropriately
- Removes invalid data (negative prices/quantities)
- Calculates revenue for each transaction
- Produces a clean, analysis-ready dataset

Project Structure
ism2411-data-cleaning-copilot/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv
│   └── processed/
│       └── sales_data_clean.csv         
├── src/
│   └── data_cleaning.py                
├── README.md                           
└── reflection.md                       

Requirements

Python 3.7+
pandas

Install dependencies:
bashpip install pandas

How to Run
Ensure sales_data_raw.csv is in the data/raw/ directory
From the project root, run:

bash   python src/data_cleaning.py

The cleaned data will be saved to data/processed/sales_data_clean.csv

What Gets Cleaned

- Column Names: Strips leading/trailing spaces and converts to lowercase with underscores (e.g., " CATEGORY" → "category")
- Data Types: Converts price and qty from strings to numeric values
- Whitespace: Strips leading/trailing spaces from all text fields
- Missing Values: Removes rows with missing prices or quantities
- Invalid Data: Filters out negative or zero prices and quantities
- New Calculations: Adds revenue column (price × qty)

Author: Jose Guilherme Brol Leal 

Created as part of ISM 2411 coursework at the University of South Florida, Muma College of Business.

License
This project is for educational purposes.
