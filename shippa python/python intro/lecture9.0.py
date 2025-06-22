class account:
    def __init__(self, balance, account):
        self.bal = balance
        self.acc_no = account

    def debit(self, amount):
        self.bal -= amount
        print("Rs.", amount, "was debitted" )
        print("total account balance is", self.bal)

    def credit(self, amount):
        self.bal += amount
        print("Rs.", amount, "was credited" )
        print("total account balance is", self.bal)

    # def get_balance(self):
    #      return self.bal

acc1 = account(10000, 740789556)
acc1.debit(500)
acc1.credit(2000)