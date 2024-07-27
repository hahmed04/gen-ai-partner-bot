import requests

class EdgarData:
    def __init__(self, file_url):
        self.file_url = file_url  # URL containing data
        self.company_data = {}  # Maps both company names and tickers to data
        
        headers = {'User-Agent': 'MLT HA hahmed3001@gmail.com'}
        response = requests.get(self.file_url, headers=headers)
        
        if response.status_code == 200:  # Checking if fetching data was successful
            data = response.json()
            for item in data.values():
                # Ensuring all keys exist and have non-empty values
                if 'cik_str' in item and 'ticker' in item and 'title' in item:
                    cik = item['cik_str']
                    ticker = item['ticker']
                    title = item['title']
                    if cik and ticker and title:
                        self.company_data[title] = (cik, ticker, title)
                        self.company_data[ticker] = (cik, ticker, title)

    # Returns a tuple with CIK, Ticker, and Name given a company name
    def name_to_cik(self, name):
        return self.company_data.get(name)

    # Returns a tuple with CIK, Ticker, and Name given a ticker symbol
    def ticker_to_cik(self, ticker):
        return self.company_data.get(ticker)

# Example usage
s = EdgarData('https://www.sec.gov/files/company_tickers.json')
print(s.ticker_to_cik("AAPL"))
