class ohid:
    def __init__(self, date, description, trans_type, amount):
        self.data =  date 
        self.description = description
        self.trans_type = trans_type
        self.amount = amount 
    
obj1 = ohid("12dec", "my b'day", "debit", "500")
print(obj1.amount)