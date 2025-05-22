# import pandas as pd
# import os
# from datetime import datetime
# from concurrent.futures import ThreadPoolExecutor, as_completed

# # Define the directory containing your stock CSV files
# input_dir = r'C:\Users\aksha\Music\Screener\Daily-Data\historical_data\successful'
# output_base_dir = r'Technicals\100EMA'

# # Function to calculate the 100-day EMA
# def calculate_ema(df, period=100):
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

# # Function to process each CSV file
# def process_csv(csv_file):
#     # Load the CSV data into a DataFrame
#     df = pd.read_csv(os.path.join(input_dir, csv_file))
    
#     # Ensure there is enough data to calculate the 100-day EMA
#     if len(df) < 100:
#         return f"Not enough data for {csv_file}. File skipped."
    
#     # Calculate the 100-day EMA
#     df_with_ema = calculate_ema(df, period=100)
    
#     # Get the current stock price (assumed to be the last closing price in the data)
#     stock_current_price = df_with_ema['Close'].iloc[-1]
    
#     # Calculate 'a' as 12% of the stock current price
#     a = 0.12 * stock_current_price
    
#     # Get the latest 100-day EMA value
#     latest_ema = df_with_ema['EMA'].iloc[-1]
    
#     # Check the condition: if stock_current_price - a < latest_ema < stock_current_price + a
#     if (stock_current_price - a) < latest_ema < (stock_current_price):
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
        
#         return f"Condition met for {stock_name}! 100-day EMA calculation completed and saved to '{output_file}'"
#     else:
#         return f"Condition not met for {stock_name}. File not saved."

# # Get the list of all CSV files in the input directory
# csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

# # Use ThreadPoolExecutor to manage threads
# with ThreadPoolExecutor(max_workers=5) as executor:
#     # Start the threads
#     futures = {executor.submit(process_csv, csv_file): csv_file for csv_file in csv_files}
    
#     # Process the results as they are completed
#     for future in as_completed(futures):
#         result = future.result()
#         print(result)

# print("All files processed.")






# import pandas as pd
# import os
# from datetime import datetime
# from multiprocessing import Pool, cpu_count

# # Define the directory containing your stock CSV files
# input_dir = r'C:\Users\aksha\Music\Screener\Daily-Data\historical_data\successful'
# output_base_dir = r'Technicals\100EMA'

# # Function to calculate the 100-day EMA
# def calculate_ema(df, period=100):
#     multiplier = 2 / (period + 1)
#     df['EMA'] = pd.NA
#     df.loc[period-1, 'EMA'] = df['Close'].iloc[:period].mean()
    
#     for i in range(period, len(df)):
#         df.loc[i, 'EMA'] = (df['Close'].iloc[i] * multiplier) + (df['EMA'].iloc[i-1] * (1 - multiplier))
    
#     return df

# # Function to process each CSV file
# def process_csv(csv_file):
#     df = pd.read_csv(os.path.join(input_dir, csv_file))
    
#     if len(df) < 100:
#         return f"Not enough data for {csv_file}. File skipped."
    
#     df_with_ema = calculate_ema(df, period=100)
#     stock_current_price = df_with_ema['Close'].iloc[-1]
#     a = 0.12 * stock_current_price
#     latest_ema = df_with_ema['EMA'].iloc[-1]
    
#     if (stock_current_price - a) < latest_ema < (stock_current_price):
#         stock_name = os.path.splitext(csv_file)[0]
#         current_date = datetime.now().strftime('%Y-%m-%d')
#         output_dir = os.path.join(output_base_dir, current_date)
#         output_file = os.path.join(output_dir, f'{stock_name}.csv')
        
#         os.makedirs(output_dir, exist_ok=True)
#         df_with_ema.to_csv(output_file, index=False)
        
#         return f"Condition met for {stock_name}! 100-day EMA calculation completed and saved to '{output_file}'"
#     else:
#         return f"Condition not met for {stock_name}. File not saved."

# # Get the list of all CSV files in the input directory
# csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

# # Use multiprocessing to process the files
# if __name__ == '__main__':
#     with Pool(processes=cpu_count()) as pool:
#         results = pool.map(process_csv, csv_files)
    
#     for result in results:
#         print(result)

#     print("All files processed.")








import pandas as pd
import os
from datetime import datetime
from multiprocessing import Pool, cpu_count

# Define the directory containing your stock CSV files
input_dir = r'C:\Users\aksha\Music\Screener\Daily-Data\historical_data\successful'
output_base_dir = r'Technicals\100EMA'

# Function to calculate the 100-day EMA
def calculate_ema(df, period=100):
    multiplier = 2 / (period + 1)
    df['EMA'] = pd.NA
    df.loc[period-1, 'EMA'] = df['Close'].iloc[:period].mean()
    
    for i in range(period, len(df)):
        df.loc[i, 'EMA'] = (df['Close'].iloc[i] * multiplier) + (df['EMA'].iloc[i-1] * (1 - multiplier))
    
    return df

# Function to process each CSV file
def process_csv(csv_file):
    # Load the CSV data into a DataFrame, skipping the header
    df = pd.read_csv(os.path.join(input_dir, csv_file), skiprows=1)
    
    if len(df) < 100:
        return f"Not enough data for {csv_file}. File skipped."
    
    df_with_ema = calculate_ema(df, period=100)
    stock_current_price = df_with_ema['Close'].iloc[-1]
    a = 0.12 * stock_current_price
    latest_ema = df_with_ema['EMA'].iloc[-1]
    
    if (stock_current_price - a) < latest_ema < (stock_current_price):
        stock_name = os.path.splitext(csv_file)[0]
        current_date = datetime.now().strftime('%Y-%m-%d')
        output_dir = os.path.join(output_base_dir, current_date)
        output_file = os.path.join(output_dir, f'{stock_name}.csv')
        
        os.makedirs(output_dir, exist_ok=True)
        df_with_ema.to_csv(output_file, index=False)
        
        return f"Condition met for {stock_name}! 100-day EMA calculation completed and saved to '{output_file}'"
    else:
        return f"Condition not met for {stock_name}. File not saved."

# Get the list of all CSV files in the input directory
csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

# Use multiprocessing to process the files
if __name__ == '__main__':
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_csv, csv_files)
    
    for result in results:
        print(result)

    print("All files processed.")
