import csv
from ticker import Ticker
from transaction import Transaction

with open('data.csv', newline='') as csv_file:
    data = csv.reader(csv_file, delimiter=' ', quotechar='|')
    ticker_dict = {} #dict()
    for row in data:
        #row_length = len(row)
        #if row_length > 0:
        tran = Transaction(row)
        symbol = tran.symbol
        if tran.is_valid():
            if symbol in ticker_dict:
                tick = ticker_dict[symbol]
                tick.add_transaction(tran)

            else:
                ticker_dict[symbol] = Ticker(symbol)

            # we will want to make this work with the raw csv from merrill edge, so we should detect row length etc

            if tran.description.startswith('Reinvestment Share(s)'):
                # this represents dividend reinvesting
                print('DIVIDEND\t for ' + symbol + ' amount: ' + tran.amount +
                      ', quantity: ' + tran.quantity + ', price: ' + tran.price)

    # after