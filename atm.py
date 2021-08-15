    class atm(object):
        def __init__(self, atmCardNumber , pin):
            self.atmCardNumber = atmCardNumber
            self.pin = pin
            self.bankBalance = 500

        def CashWithdrawal(self):
            withdrawal = int(input("Enter the amount to be withdrawn- "))
            if(withdrawal<self.bankBalance):
                self.bankBalance = self.bankBalance - withdrawal 
                print("You have withdrawn - ",withdrawal,"\n","Your balance - ",self.bankBalance)
            else:
                print("You dont have enough money")                          

        def BankBalanceEnquiry(self , bankBalance):
            print("The balance - ",self.bankBalance)

        def BankDeposit(self , bankBalance):
            deposit = int(input("Enter the amount to be deposited- "))
            self.bankBalance = deposit + self.bankBalance
            print("Ur bank balance is now- ",self.balance)    


Shaman = atm(854903, 9403849)
print(Shaman.CashWithdrawal())
print(Shaman.BankBalanceEnquiry())
print(Shaman.BankDeposit())
                    