# import pandas as pd

# # Load the CSV data into a DataFrame
# df = pd.read_csv(r'C:\Users\aksha\Music\Screener\Daily-Data\historical_data\successful\MAZDOCK.csv')

# # Function to calculate the 9-day EMA
# def calculate_ema(df, period=9):
#     # Calculate the multiplier
#     multiplier = 2 / (period + 1)
    
#     # Calculate the initial EMA (first EMA is just the SMA of the first 'period' days)
#     df['EMA'] = 0
#     df['EMA'].iloc[period-1] = df['Close'].iloc[:period].mean()
    
#     # Calculate EMA for the rest of the data
#     for i in range(period, len(df)):
#         df['EMA'].iloc[i] = (df['Close'].iloc[i] * multiplier) + (df['EMA'].iloc[i-1] * (1 - multiplier))
    
#     return df

# # Calculate the EMA
# df_with_ema = calculate_ema(df, period=9)

# # Optional: Save the DataFrame with EMA to a new CSV file
# df_with_ema.to_csv('data_with_ema.csv', index=False)

# print("EMA calculation completed and saved to 'data_with_ema.csv'")







# from datetime import datetime
# import pandas as pd
# import os

# # Load the CSV data into a DataFrame
# df = pd.read_csv(r'C:\Users\aksha\Music\Screener\Daily-Data\historical_data\successful\MAZDOCK.csv')

# # Function to calculate the 9-day EMA
# def calculate_ema(df, period=9):
#     # Calculate the multiplier
#     multiplier = 2 / (period + 1)
    
#     # Calculate the initial EMA (first EMA is just the SMA of the first 'period' days)
#     df['EMA'] = 0
#     df['EMA'].iloc[period-1] = df['Close'].iloc[:period].mean()
    
#     # Calculate EMA for the rest of the data
#     for i in range(period, len(df)):
#         df['EMA'].iloc[i] = (df['Close'].iloc[i] * multiplier) + (df['EMA'].iloc[i-1] * (1 - multiplier))
    
#     return df

# # Calculate the EMA
# df_with_ema = calculate_ema(df, period=9)

# # Get the current date
# current_date = datetime.now().strftime('%Y-%m-%d')

# # Define the directory and file name
# output_dir = os.path.join('technicals', '9EMA', current_date)
# output_file = os.path.join(output_dir, 'data_with_ema.csv')

# # Create the directory if it doesn't exist
# os.makedirs(output_dir, exist_ok=True)

# # Save the DataFrame with EMA to the specified folder
# df_with_ema.to_csv(output_file, index=False)

# print(f"EMA calculation completed and saved to '{output_file}'")






# Working code with 12% condition
# import pandas as pd
# import os
# from datetime import datetime

# # Load the CSV data into a DataFrame
# df = pd.read_csv(r'C:\Users\aksha\Music\Screener\Daily-Data\historical_data\successful\MAZDOCK.csv')

# # Function to calculate the 9-day EMA
# def calculate_ema(df, period=9):
#     # Calculate the multiplier
#     multiplier = 2 / (period + 1)
    
#     # Calculate the initial EMA (first EMA is just the SMA of the first 'period' days)
#     df['EMA'] = 0
#     df['EMA'].iloc[period-1] = df['Close'].iloc[:period].mean()
    
#     # Calculate EMA for the rest of the data
#     for i in range(period, len(df)):
#         df['EMA'].iloc[i] = (df['Close'].iloc[i] * multiplier) + (df['EMA'].iloc[i-1] * (1 - multiplier))
    
#     return df

# # Calculate the EMA
# df_with_ema = calculate_ema(df, period=9)

# # Get the current stock price (assumed to be the last closing price in the data)
# stock_current_price = df_with_ema['Close'].iloc[-1]

# # Calculate 'a' as 12% of the stock current price
# a = 0.12 * stock_current_price

# # Get the latest 9-day EMA value
# latest_ema = df_with_ema['EMA'].iloc[-1]

# # Check the condition: if stock_current_price - a < latest_ema < stock_current_price + a
# if (stock_current_price - a) < latest_ema < (stock_current_price + a):
#     # Get the current date
#     current_date = datetime.now().strftime('%Y-%m-%d')
    
#     # Define the directory and file name
#     output_dir = os.path.join('technicals', '9EMA', current_date)
#     output_file = os.path.join(output_dir, 'data_with_ema.csv')
    
#     # Create the directory if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)
    
#     # Save the DataFrame with EMA to the specified folder
#     df_with_ema.to_csv(output_file, index=False)
    
#     print(f"Condition met! EMA calculation completed and saved to '{output_file}'")
# else:
#     print("Condition not met. File not saved.")






# import pandas as pd
# import os
# from datetime import datetime

# # Load the CSV data into a DataFrame
# df = pd.read_csv(r'C:\Users\aksha\Music\Screener\Daily-Data\historical_data\successful\MAZDOCK.csv')

# # Function to calculate the 9-day EMA
# def calculate_ema(df, period=9):
#     # Calculate the multiplier
#     multiplier = 2 / (period + 1)
    
#     # Initialize the EMA column
#     df['EMA'] = pd.NA
    
#     # Calculate the initial EMA (first EMA is just the SMA of the first 'period' days)
#     df.loc[period-1, 'EMA'] = df['Close'].iloc[:period].mean()
    
#     # Calculate EMA for the rest of the data
#     for i in range(period, len(df)):
#         df.loc[i, 'EMA'] = (df['Close'].iloc[i] * multiplier) + (df['EMA'].iloc[i-1] * (1 - multiplier))
    
#     return df

# # Calculate the EMA
# df_with_ema = calculate_ema(df, period=9)

# # Get the current stock price (assumed to be the last closing price in the data)
# stock_current_price = df_with_ema['Close'].iloc[-1]

# # Calculate 'a' as 12% of the stock current price
# a = 0.12 * stock_current_price

# # Get the latest 9-day EMA value
# latest_ema = df_with_ema['EMA'].iloc[-1]

# # Check the condition: if stock_current_price - a < latest_ema < stock_current_price + a
# if (stock_current_price - a) < latest_ema < (stock_current_price + a):
#     # Get the current date
#     current_date = datetime.now().strftime('%Y-%m-%d')
    
#     # Define the directory and file name
#     output_dir = os.path.join('technicals', '9EMA', current_date)
#     output_file = os.path.join(output_dir, 'data_with_ema.csv')
    
#     # Create the directory if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)
    
#     # Save the DataFrame with EMA to the specified folder
#     df_with_ema.to_csv(output_file, index=False)
    
#     print(f"Condition met! EMA calculation completed and saved to '{output_file}'")
# else:
#     print("Condition not met. File not saved.")






# working code perfectly without multiple threading
# import pandas as pd
# import os
# from datetime import datetime

# # Define the directory containing your stock CSV files
# input_dir = r'C:\Users\aksha\Music\Screener\Daily-Data\historical_data\successful'
# output_base_dir = r'Technicals\9EMA'

# # Function to calculate the 9-day EMA
# def calculate_ema(df, period=9):
#     # Calculate the multiplier
#     multiplier = 2 / (period + 1)
    
#     # Initialize the EMA column
#     df['EMA'] = pd.NA
    
#     # Calculate the initial EMA (first EMA is just the SMA of the first 'period' days)
#     df.loc[period-1, 'EMA'] = df['Close'].iloc[:period].mean()
    
#     # Calculate EMA for the rest of the data
#     for i in range(period, len(df)):
#         df.loc[i, 'EMA'] = (df['Close'].iloc[i] * multiplier) + (df['EMA'].iloc[i-1] * (1 - multiplier))
    
#     return df

# # Get the list of all CSV files in the input directory
# csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

# # Iterate through each CSV file and calculate the EMA
# for csv_file in csv_files:
#     # Load the CSV data into a DataFrame
#     df = pd.read_csv(os.path.join(input_dir, csv_file))
    
#     # Calculate the EMA
#     df_with_ema = calculate_ema(df, period=9)
    
#     # Get the current stock price (assumed to be the last closing price in the data)
#     stock_current_price = df_with_ema['Close'].iloc[-1]
    
#     # Calculate 'a' as 12% of the stock current price
#     a = 0.12 * stock_current_price
    
#     # Get the latest 9-day EMA value
#     latest_ema = df_with_ema['EMA'].iloc[-1]
    
#     # Check the condition: if stock_current_price - a < latest_ema < stock_current_price + a
#     if (stock_current_price - a) < latest_ema < (stock_current_price + a):
#         # Extract the stock name from the filename (remove the .csv extension)
#         stock_name = os.path.splitext(csv_file)[0]
        
#         # Get the current date
#         current_date = datetime.now().strftime('%Y-%m-%d')
        
#         # Define the output directory and file name
#         output_dir = os.path.join(output_base_dir, current_date)
#         output_file = os.path.join(output_dir, f'{stock_name}.csv')
        
#         # Create the directory if it doesn't exist
#         os.makedirs(output_dir, exist_ok=True)
        
#         # Save the DataFrame with EMA to the specified folder
#         df_with_ema.to_csv(output_file, index=False)
        
#         print(f"Condition met for {stock_name}! EMA calculation completed and saved to '{output_file}'")
#     else:
#         print(f"Condition not met for {stock_name}. File not saved.")









import pandas as pd
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define the directory containing your stock CSV files
input_dir = r'C:\Users\aksha\Music\Screener\Daily-Data\historical_data\successful'
output_base_dir = r'Technicals\9EMA'

# Function to calculate the 9-day EMA
def calculate_ema(df, period=9):
    # Calculate the multiplier
    multiplier = 2 / (period + 1)
    
    # Initialize the EMA column
    df['EMA'] = pd.NA
    
    # Calculate the initial EMA (first EMA is just the SMA of the first 'period' days)
    df.loc[period-1, 'EMA'] = df['Close'].iloc[:period].mean()
    
    # Calculate EMA for the rest of the data
    for i in range(period, len(df)):
        df.loc[i, 'EMA'] = (df['Close'].iloc[i] * multiplier) + (df['EMA'].iloc[i-1] * (1 - multiplier))
    
    return df

# Function to process each CSV file
def process_csv(csv_file):
    # Load the CSV data into a DataFrame
    df = pd.read_csv(os.path.join(input_dir, csv_file))
    
    # Calculate the EMA
    df_with_ema = calculate_ema(df, period=9)
    
    # Get the current stock price (assumed to be the last closing price in the data)
    stock_current_price = df_with_ema['Close'].iloc[-1]
    
    # Calculate 'a' as 12% of the stock current price
    a = 0.12 * stock_current_price
    
    # Get the latest 9-day EMA value
    latest_ema = df_with_ema['EMA'].iloc[-1]
    
    # Check the condition: if stock_current_price - a < latest_ema < stock_current_price + a
    if (stock_current_price - a) < latest_ema < (stock_current_price):
        # Extract the stock name from the filename (remove the .csv extension)
        stock_name = os.path.splitext(csv_file)[0]
        
        # Get the current date
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        # Define the output directory and file name
        output_dir = os.path.join(output_base_dir, current_date)
        output_file = os.path.join(output_dir, f'{stock_name}.csv')
        
        # Create the directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Save the DataFrame with EMA to the specified folder
        df_with_ema.to_csv(output_file, index=False)
        
        return f"Condition met for {stock_name}! EMA calculation completed and saved to '{output_file}'"
    else:
        return f"Condition not met for {stock_name}. File not saved."

# Get the list of all CSV files in the input directory
csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

# Use ThreadPoolExecutor to manage threads
with ThreadPoolExecutor(max_workers=10) as executor:
    # Start the threads
    futures = {executor.submit(process_csv, csv_file): csv_file for csv_file in csv_files}
    
    # Process the results as they are completed
    for future in as_completed(futures):
        result = future.result()
        print(result)

print("All files processed.")
