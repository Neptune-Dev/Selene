class u_table():

    def __init__(self, name, rows):
        self.name = name
        self.rows = rows

    def add_row(self, row):
        self.rows[row.get_key()] = row


    def get_name(self):
        return self.name

    def get_rows(self):
        return self.rows

    def get_row(self, name):
        self.get_rows()[name]