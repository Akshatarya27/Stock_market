import os
import logging
import pandas as pd
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random
from datetime import datetime

# Configuration
START_DATE = "2020-01-01"
END_DATE = datetime.today().strftime("%Y-%m-%d")
MAX_WORKERS = 5
MAX_RETRIES = 3
SYMBOL_URL = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"

# Configure logging
logging.basicConfig(
    filename='stock_data_downloader_new.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

def setup_directories():
    """Create output directories with logging"""
    directories = ["historical_data_thread", "market_caps_thread"]
    for dir in directories:
        os.makedirs(dir, exist_ok=True)
        logger.info(f"Created directory: {dir}")

def process_symbol(symbol):
    """Process individual symbol with retry logic"""
    attempts = 0
    last_exception = None
    
    while attempts < MAX_RETRIES:
        try:
            logger.debug(f"Processing {symbol} (Attempt {attempts+1})")
            ticker = yf.Ticker(f"{symbol}.NS")
            data = ticker.history(start=START_DATE, end=END_DATE)
            
            if not data.empty:
                file_path = f"historical_data_thread/{symbol}.csv"
                data.to_csv(file_path)
                logger.info(f"Successfully saved {symbol}")
                
                market_cap = ticker.info.get('marketCap', None)
                return {"Symbol": symbol, "MarketCap": market_cap}
            
            logger.warning(f"No data available for {symbol}")
            return None
            
        except Exception as e:
            attempts += 1
            last_exception = e
            if attempts < MAX_RETRIES:
                sleep_time = (2 ** attempts) + random.uniform(0, 1)
                logger.warning(f"Retry #{attempts} for {symbol} - Sleeping {sleep_time:.2f}s")
                time.sleep(sleep_time)
        finally:
            # Fixed 0.6 second delay after each attempt
            time.sleep(0.7)
    
    logger.error(f"Failed {symbol} after {MAX_RETRIES} attempts")
    return None

def main():
    """Main execution function"""
    logger.info("Starting NSE data download process")
    setup_directories()
    
    try:
        logger.info(f"Fetching symbols from {SYMBOL_URL}")
        symbols = pd.read_csv(SYMBOL_URL)["SYMBOL"].tolist()
        total_symbols = len(symbols)
        logger.info(f"Loaded {total_symbols} symbols")
        
        market_caps = []
        processed_count = 0
        
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(process_symbol, sym): sym for sym in symbols}
            
            logger.info(f"Started processing with {MAX_WORKERS} workers")
            start_time = time.time()
            
            for future in futures:
                result = future.result()
                if result:
                    market_caps.append(result)
                processed_count += 1
                
                if processed_count % 50 == 0:
                    elapsed = time.time() - start_time
                    logger.info(
                        f"Progress: {processed_count}/{total_symbols} "
                        f"({(processed_count/total_symbols)*100:.1f}%) "
                        f"Elapsed: {elapsed/60:.1f} mins"
                    )
        
        if market_caps:
            output_file = "market_caps_thread/market_caps.csv"
            pd.DataFrame(market_caps).to_csv(output_file, index=False)
            logger.info(f"Saved market caps for {len(market_caps)} symbols")
        
        success_count = len(market_caps)
        elapsed_total = (time.time() - start_time) / 60
        logger.info(f"Process completed: {success_count} success, {total_symbols-success_count} failures")
        logger.info(f"Total time: {elapsed_total:.1f} minutes")
        
    except Exception as e:
        logger.critical(f"Fatal error: {str(e)}")
        raise

if __name__ == "__main__":
    main()