class Ticker:
    def __init__(self, ticker):
        self.ticker = ticker
        self.transaction_list = []

    def add_transaction(self, transaction):
        self.transaction_list.append(transaction)
        print('transaction added for %s, total = %d' % (self.ticker, len(self.transaction_list)))

    def get_total_dividend(self):
        return 3

    # we need a way to translate between ticker and company name (PEP and PEPSICO INC)

    # in order to calculate the DRIP data we need 3 consecutive transactions (from newest to oldest)
    # 1. Reinvestment Share(s) PEPSICO INC PRINCIPAL REINV AMOUNT
    # 2. Reinvestment Program PEPSICO INC
    # 3. Dividend PEPSICO INC HOLDING
    # which will make up one "DRIP"