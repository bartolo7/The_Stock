import requests
from utility import Utility


class Security:

    def __init__(self, security_symbol=None):
        self.security_symbol = security_symbol

    """#################### END POINTS IEXTRADING ############################"""

    # Base URL
    def create_url(self, endpoint=None):
        url = 'https://api.iextrading.com/1.0/stock/{}/{}'.format(self.security_symbol, endpoint)
        return url

    # URL COMPANY
    def request_company(self):
        url = self.create_url('company')
        response = requests.get(url)
        return response.json()

    # URL DIVIDEND
    def retrieve_dividend_5_years_data(self):
        url = self.create_url('dividends/5y')
        response = requests.get(url)
        return response.json()

    # URL STATS
    def request_stats(self):
        url = self.create_url('stats')
        response = requests.get(url)
        return response.json()

    # URL Earnings
    def request_earnings(self):
        url = self.create_url('earnings')
        response = requests.get(url)
        return response.json()

    # URL Delayed Quote
    def request_delayed_share_quote(self):
        url = self.create_url('delayed-quote')
        response = requests.get(url)
        return response.json()

    """#################### END POINTS IEXTRADING ############################"""

    def retrieve_company_symbol(self):
        data = self.request_company()
        if 'symbol' in data:
            return data['symbol']
        else:
            return 'Error: No symbol'

    def average_dividend_5_years(self):
        data_5y = self.retrieve_dividend_5_years_data()
        if data_5y:
            dividends = list(map(lambda x: x['amount'], data_5y))
            avg_dividend = Utility.calculate_avg_list_of_numbers(dividends)
            avg_dividend_5_year = avg_dividend * (len(dividends) / 5)
            return avg_dividend_5_year

    def generate_market_cap_value(self):
        data = self.request_stats()
        if data:
            market_cap = data['marketcap']
            return Utility.generate_readable_number_with_decimal_description(market_cap)

    def generate_beta_value(self):
        data = self.request_stats()
        if data:
            beta = data['beta']
            return round(beta, 2)

    def generate_dividend_rate(self):
        data = self.request_stats()
        if data:
            dividend_rate = data['dividendRate']
            return round(dividend_rate, 2)

    def generate_price_to_book_value(self):
        data = self.request_stats()
        if data:
            price_to_book_value = data['priceToBook']
            return price_to_book_value

    def retrieve_company_name(self):
        data = self.request_stats()
        if 'companyName' in data:
            return data['companyName']
        else:
            return 'Error: No company name'

    def retrieve_list_earnings_per_share_period(self):
        data = self.request_earnings()
        if 'earnings' in data:
            earnings = data['earnings']
            list_earnings_per_share = [x['actualEPS'] for x in earnings]
            return list_earnings_per_share

    def retrieve_price_per_share(self):
        data = self.request_delayed_share_quote()
        if 'delayedPrice' in data:
            return data['delayedPrice']

    def generate_price_earnings_value(self):
        price = self.retrieve_price_per_share()
        earnings_share_list = self.retrieve_list_earnings_per_share_period()
        value = sum(earnings_share_list)
        if price and value:
            price_earnings = float(price) / float(value)
            return round(price_earnings, 2)
