class Transaction:
    def __init__(self, data):
        # split data on ',' and assign the properties
        data_array = ' '.join(data).replace('"','').split(',')
        # we could read in the header of the csv file but for now
        # we will just hard code the order of the file
        self.trade_date = data_array[0]
        self.settlement_data = data_array[1]
        self.account = data_array[2]
        self.description = data_array[3]
        self.type = data_array[4]
        self.symbol = data_array[5].strip()
        self.quantity = data_array[6]
        self.price = data_array[7]
        self.amount = data_array[8]

    def is_valid(self):
        return self.symbol and not self.symbol.isnumeric()
