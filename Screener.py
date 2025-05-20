# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os

# # Path to your WebDriver
# driver_path = r'C:\Users\aksha\OneDrive\Documents\Stock_market\chromedriver-win64\chromedriver.exe'


# # Screener.in login credentials
# email = 'rituarya1004@gmail.com'
# password = 'Ritudidi1!'

# # List of company symbols
# company_symbols = [
#     'RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ITC', 
#     'HINDUNILVR', 'ICICIBANK', 'KOTAKBANK', 'LT', 
#     'SBIN', 'BHARTIARTL', 'ASIANPAINT', 'MARUTI', 
#     'HDFC', 'BAJFINANCE', 'ONGC', 'TATAMOTORS', 
#     'ADANIGREEN', 'ADANIPORTS', 'NTPC'
# ]

# # Directory to save downloaded files
# download_dir = r'C:\Users\aksha\Music\Screener\fundamentals'

# # Ensure the download directory exists
# if not os.path.exists(download_dir):
#     os.makedirs(download_dir)

# # Set Chrome options to change the download directory
# options = Options()
# options.add_experimental_option("prefs", {
#     "download.default_directory": download_dir  # Set the custom download directory
# })

# # Initialize the WebDriver with the service object and options
# service = Service(executable_path=driver_path)
# driver = webdriver.Chrome(service=service, options=options)

# try:
#     # Open Screener.in login page
#     driver.get('https://www.screener.in/login/')

#     # Enter email and password to log in
#     email_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "username"))
#     )
#     email_input.send_keys(email)

#     password_input = driver.find_element(By.NAME, "password")
#     password_input.send_keys(password)
    
#     # Submit the login form
#     login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
#     login_button.click()

#     # Wait until login is complete by checking for the presence of the user's profile menu
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/account/")]'))
#     )

#     # Loop through each company symbol to download data
#     for company_symbol in company_symbols:
#         # Navigate to the company's page
#         company_url = f'https://www.screener.in/company/{company_symbol}/'
#         driver.get(company_url)

#         # Click the Export to Excel button
#         # WebDriverWait(driver, 5).until(
#         # driver.find_element(By.XPATH, "/html/body/main/div[3]/div[1]/form/button").click()
#         # )
#         export_button = WebDriverWait(driver, 10).until(
#          EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[3]/div[1]/form/button"))
#         )
#         export_button.click()
#         # Wait for the file to download (adjust this time as needed)
#         time.sleep(4)

#         print(f'Exported data for {company_symbol} to {download_dir}')
    
# finally:
#     # Close the browser
#     driver.quit()












# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os
# import csv

# # Path to your WebDriver
# driver_path = r'C:\Users\aksha\Music\Screener\chromedriver-win64\chromedriver.exe'

# # Screener.in login credentials
# email = 'rituarya1004@gmail.com'
# password = 'Ritudidi1!'

# # Path to CSV file containing symbols
# csv_path = r'C:\Users\aksha\Music\Screener\nse_symbol.csv'  # Update this path if needed

# # Read symbols from CSV
# company_symbols = []
# with open(csv_path, 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)  # Skip header row
#     for row in reader:
#         if row:  # Check if row is not empty
#             company_symbols.append(row[0])  # Assuming SYMBOL is first column

# # Directory to save downloaded files
# download_dir = r'C:\Users\aksha\Music\Screener\fundamentals'

# # Ensure the download directory exists
# if not os.path.exists(download_dir):
#     os.makedirs(download_dir)

# # Set Chrome options to change the download directory
# options = Options()
# options.add_experimental_option("prefs", {
#     "download.default_directory": download_dir,
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "safebrowsing.enabled": True
# })

# # Initialize the WebDriver with the service object and options
# service = Service(executable_path=driver_path)
# driver = webdriver.Chrome(service=service, options=options)

# try:
#     # Open Screener.in login page
#     driver.get('https://www.screener.in/login/')

#     # Enter email and password to log in
#     email_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "username"))
#     )
#     email_input.send_keys(email)

#     password_input = driver.find_element(By.NAME, "password")
#     password_input.send_keys(password)
    
#     # Submit the login form
#     login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
#     login_button.click()

#     # Wait until login is complete
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/account/")]'))
#     )

#     # Loop through each company symbol to download data
#     for company_symbol in company_symbols:
#         try:
#             # Navigate to the company's page
#             company_url = f'https://www.screener.in/company/{company_symbol}/'
#             driver.get(company_url)

#             # Click the Export to Excel button
#             export_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Export to Excel')]"))
#             )
#             export_button.click()
            
#             # Wait for the file to download
#             time.sleep(4)  # Adjust this time based on your internet speed
            
#             print(f'Downloaded data for {company_symbol} to {download_dir}')
            
#         except Exception as e:
#             print(f'Error processing {company_symbol}: {str(e)}')
#             continue
    
# finally:
#     # Close the browser
#     driver.quit()
#     print("All downloads completed. Browser closed.")













# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os
# import csv

# # Get current directory path
# current_dir = os.path.dirname(__file__)

# # -------------------------------
# # 1. Path Configuration (Relative Paths)
# # -------------------------------
# # ChromeDriver in current directory
# driver_path = os.path.join(current_dir, 'chromedriver.exe')  # Ensure chromedriver is in the same folder

# # CSV file in current directory
# csv_path = os.path.join(current_dir, 'nse_symbol.csv')

# # Download directory (will be created in current directory)
# download_dir = os.path.join(current_dir, 'fundamentals')

# # -------------------------------
# # 2. File Validation
# # -------------------------------
# # Check for required files
# if not os.path.exists(driver_path):
#     raise FileNotFoundError("Chromedriver not found in script directory. Please add chromedriver.exe")

# if not os.path.exists(csv_path):
#     raise FileNotFoundError("nse_symbol.csv not found in script directory")

# # Create fundamentals directory if needed
# if not os.path.exists(download_dir):
#     os.makedirs(download_dir)
#     print(f"Created download directory: {download_dir}")

# # -------------------------------
# # 3. WebDriver Setup
# # -------------------------------
# options = Options()
# options.add_experimental_option("prefs", {
#     "download.default_directory": download_dir,
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "safebrowsing.enabled": True
# })

# service = Service(executable_path=driver_path)
# driver = webdriver.Chrome(service=service, options=options)

# # -------------------------------
# # 4. Credentials (User should fill these)
# # -------------------------------
# email = 'rituarya1004@gmail.com'  # Consider making these input() prompts
# password = 'Ritudidi1!'          # or environment variables

# # -------------------------------
# # 5. CSV Processing
# # -------------------------------
# try:
#     with open(csv_path, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         header = next(reader)  # Read header
        
#         # Validate CSV format
#         if header[0].upper() != 'SYMBOL':
#             raise ValueError("CSV format incorrect. First column should be 'SYMBOL'")
        
#         company_symbols = [row[0] for row in reader if row]

# except Exception as e:
#     print(f"Error reading CSV: {str(e)}")
#     driver.quit()
#     exit()

# # -------------------------------
# # 6. Main Script Logic
# # -------------------------------
# try:
#     # [Keep the login and download logic from previous versions]
#     # Example:
#     driver.get('https://www.screener.in/login/')
    
#     # Login logic...
#     # File download logic...
    
# finally:
#     driver.quit()








# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os
# import csv

# # Get current script directory
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Configuration - Relative Paths
# DRIVER_NAME = 'chromedriver.exe'  # Must be in same directory
# CSV_NAME = 'nse_symbols.csv'       # CSV with SYMBOL header
# DOWNLOAD_FOLDER = 'fundamentals'  # Will be created automatically
# username = 'rituarya1004@gmai.com'
# password = 'Ritudidi1!'

# # Path Setup
# driver_path = os.path.join(current_dir, DRIVER_NAME)
# csv_path = os.path.join(current_dir, CSV_NAME)
# download_dir = os.path.join(current_dir, DOWNLOAD_FOLDER)

# def validate_environment():
#     """Check for required files and setup directory"""
#     if not os.path.exists(driver_path):
#         raise FileNotFoundError(f"ChromeDriver not found at: {driver_path}")
    
#     if not os.path.exists(csv_path):
#         raise FileNotFoundError(f"CSV file not found at: {csv_path}")
    
#     os.makedirs(download_dir, exist_ok=True)
#     print(f"Download directory ready: {download_dir}")

# def read_symbols():
#     """Read symbols from CSV with validation"""
#     symbols = []
#     with open(csv_path, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         try:
#             header = next(reader)
#             if header[0].upper() != 'SYMBOL':
#                 raise ValueError("First column must be 'SYMBOL'")
            
#             symbols = [row[0].strip() for row in reader if row and row[0].strip()]
            
#         except StopIteration:
#             raise ValueError("CSV file is empty")
    
#     if not symbols:
#         raise ValueError("No symbols found in CSV file")
    
#     return symbols

# def configure_chrome():
#     """Set up Chrome options for downloads"""
#     options = Options()
#     options.add_argument("--headless=new")  # Remove this line to see browser
#     options.add_experimental_option("prefs", {
#         "download.default_directory": download_dir,
#         "download.prompt_for_download": False,
#         "download.directory_upgrade": True,
#         "safebrowsing.enabled": True
#     })
#     return options

# def main():
#     # Validate environment first
#     validate_environment()
    
#     # Read symbols from CSV
#     try:
#         company_symbols = read_symbols()
#         print(f"Found {len(company_symbols)} symbols in CSV")
#     except Exception as e:
#         print(f"CSV Error: {str(e)}")
#         return

#     # Chrome configuration
#     options = configure_chrome()
#     service = Service(executable_path=driver_path)
#     driver = webdriver.Chrome(service=service, options=options)

#     try:
#         # Login to Screener.in
#         driver.get('https://www.screener.in/login/')
        
#         # Enter credentials
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.NAME, "username"))
#         ).send_keys(username)  # Replace with your email
        
#         driver.find_element(By.NAME, "password").send_keys(password)  # Replace with your password
        
#         # Submit login
#         driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        
#         # Verify login
#         WebDriverWait(driver, 15).until(
#             EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/account/")]'))
#         )
#         print("Login successful")

#         # Process each symbol
#         for symbol in company_symbols:
#             try:
#                 print(f"Processing {symbol}...")
#                 driver.get(f'https://www.screener.in/company/{symbol}/')
                
#                 # Wait for page load
#                 WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, 'div.company-ratios'))
#                 )
                
#                 # Click export button
#                 export_btn = WebDriverWait(driver, 10).until(
#                     EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Export to Excel")]'))
#                 )
#                 export_btn.click()
                
#                 # Brief pause for download
#                 time.sleep(4)
                
#             except Exception as e:
#                 print(f"Failed to process {symbol}: {str(e)}")
#                 continue

#         print("Processing completed. Closing browser...")

#     finally:
#         driver.quit()
#         print("Browser closed. Downloads available in:", download_dir)

# if __name__ == "__main__":
#     main()




# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os
# import csv  # Import the csv module

# # Path to your WebDriver
# driver_path = r'C:\Users\aksha\OneDrive\Documents\Stock_market\chromedriver-win64\chromedriver.exe'

# # Path to the CSV file containing symbols (UPDATE THIS PATH)
# csv_path = r'C:\Users\aksha\OneDrive\Documents\Stock_market\nse_symbols.csv'

# # Read company symbols from CSV
# company_symbols = []
# with open(csv_path, 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         company_symbols.append(row['SYMBOL'])  # Ensure header is 'SYMBOLS'

# # Screener.in login credentials
# email = 'rituarya1004@gmail.com'
# password = 'Ritudidi1!'

# # Directory to save downloaded files
# download_dir = r'C:\Users\aksha\OneDrive\Documents\Stock_market\fundamentals'

# # Ensure the download directory exists
# if not os.path.exists(download_dir):
#     os.makedirs(download_dir)

# # Set Chrome options to change the download directory
# options = Options()
# options.add_experimental_option("prefs", {
#     "download.default_directory": download_dir  # Custom download directory
# })

# # Initialize the WebDriver
# service = Service(executable_path=driver_path)
# driver = webdriver.Chrome(service=service, options=options)

# try:
#     # Open Screener.in login page
#     driver.get('https://www.screener.in/login/')

#     # Enter email and password to log in
#     email_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "username"))
#     )
#     email_input.send_keys(email)

#     password_input = driver.find_element(By.NAME, "password")
#     password_input.send_keys(password)
    
#     # Submit the login form
#     login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
#     login_button.click()

#     # Wait until login is complete
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/account/")]'))
#     )

#     # Loop through each company symbol to download data
#     for symbol in company_symbols:
#         company_url = f'https://www.screener.in/company/{symbol}/'
#         driver.get(company_url)

#         # Click the Export to Excel button
#         export_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[3]/div[1]/form/button"))
#         )
#         export_button.click()
        
#         # Wait for the file to download
#         time.sleep(4)
#         print(f'Exported data for {symbol} to {download_dir}')

# finally:
#     # Close the browser
#     driver.quit()










from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import csv

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Configure paths relative to the script location
driver_path = os.path.join(script_dir, 'chromedriver.exe')  # Place chromedriver in script directory
csv_path = os.path.join(script_dir, 'nse_symbols.csv')      # CSV in script directory
download_dir = os.path.join(script_dir, 'fundamentals')     # Downloads will go here

# Ensure download directory exists
os.makedirs(download_dir, exist_ok=True)

# Read company symbols from CSV
company_symbols = []
try:
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        if 'SYMBOL' not in reader.fieldnames:
            raise ValueError("CSV file must contain a 'SYMBOL' header column")
        company_symbols = [row['SYMBOL'] for row in reader]
except FileNotFoundError:
    print(f"Error: CSV file not found at {csv_path}")
    exit()

# Configure Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
})

# Initialize WebDriver
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Login to Screener.in
    driver.get('https://www.screener.in/login/')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    ).send_keys('rituarya1004@gmail.com')
    
    driver.find_element(By.NAME, "password").send_keys('Ritudidi1!')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Verify login success
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/account/")]'))
    )

    # Process each symbol
    for symbol in company_symbols:
        driver.get(f'https://www.screener.in/company/{symbol}/')
        try:
            export_button = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[3]/div[1]/form/button"))
        )
            export_button.click()
            time.sleep(4)  # Simple download wait
            print(f"Successfully downloaded: {symbol}")
        except Exception as e:
            print(f"Failed to download {symbol}: {str(e)}")

finally:
    driver.quit()