from flask import Flask, render_template, request
from utility import Security_iextrading

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.errorhandler(500)
@app.route('/Stock-Symbol/', methods=["GET"])
def get_stock_symbol():
    the_symbol = request.args.get('symbol', default='*', type=str)
    if not the_symbol:
        return render_template('index.html')
    else:
        try:
            stock = Security_iextrading.Security(the_symbol)
            return render_template('result.html', stock_symbol=stock.retrieve_company_symbol(),
                                   stock_name=stock.retrieve_company_name(),
                                   dividend_yield=str(stock.generate_dividend_rate()),
                                   dividend_5year=str(stock.average_dividend_5_years()),
                                   price_book_value=str(stock.generate_price_to_book_value()),
                                   market_cap=str(stock.generate_market_cap_value()),
                                   price_earnings=str(stock.generate_price_earnings_value()))
        except ValueError:
            return "Oops!  That was no valid symbol.  Try again..."


if __name__ == '__main__':
    app.run(host='0.0.0.0')
