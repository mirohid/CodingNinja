class ExpenseTracker:

    expense_tracker_version = 0.1

    def __init__(self, tracker_catagory, opening_balance, budget):
        self.tracker_catagory = tracker_catagory
        self.opening_balance = opening_balance
        self.budget = budget

obj1 = ExpenseTracker("home",3000,10000)
print(obj1.tracker_catagory)
obj2 = ExpenseTracker("shopping", 1000,5000)
print(obj2.tracker_catagory)
print(obj2.__dict__)