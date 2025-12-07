Project Reflection

What Copilot Generated

For this project, I used Copilot mainly to help outline the core cleaning functions. I began each function by writing a short comment explaining what I wanted to do, and once I typed the function name, Copilot suggested a basic structure for it. In the clean_column_names() function, I wrote that I needed the column names in lowercase and with underscores, and Copilot suggested using .str.lower() and .str.replace(), which matched what I needed. The same thing happened with handling missing values. I explained that price and quantity needed to be numeric and that missing values should be removed. Copilot suggested converting them with pd.to_numeric(errors="coerce") and using dropna() to target those specific columns. It also generated most of the logic for removing invalid rows using boolean filtering.

What I Modified

Even though Copilot gave me a good starting point, I had to adjust several parts to make the cleaning process work correctly for my dataset. The raw file had column names with random spaces at the beginning, so I added .str.strip() to fix that because Copilot did not include it. I also added print statements in the missing values function because I wanted to see how many rows were removed at each step. This made the cleaning process feel more transparent, which is something I value when working on analytics projects. In the invalid row function, I expanded the logic so that negative quantities and prices were removed as well, since those values would break any revenue analysis. These changes helped the script fit both the dataset and the business context better.

What I Learned

This project showed me how messy real-world data can be. Even a small sales file had inconsistent formatting, unexpected whitespace, and numeric values stored as text. I realized how important it is to clean and validate data before trying to analyze it or build dashboards from it. This connects directly to the work I enjoy doing in business analytics, where clean data is the foundation of everything else.

Using Copilot taught me how to treat AI as a supportive tool instead of something to rely on completely. It was helpful for generating common pandas patterns, especially when I described what I wanted in comments. At the same time, Copilot did not understand the specific issues in my dataset, and it could not make the business decisions about what should be removed or corrected. Those choices had to come from me. This assignment made me more confident in writing my own Python code and in knowing how to combine my reasoning with AI assistance in a responsible way.
