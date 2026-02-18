
class BankAccount:

#   Rate of Intrest
    ROI = 10.5
    
    def __init__(self,AccountName,AccountBal):
        self.AccName = AccountName
        self.AccBal = AccountBal
        

    def Display(self):
        print("Account Holder is : ",self.AccName,", Current Balance is : ",self.AccBal)       

    def Deposit(self,Amount = 0):
        NewTotal = Amount
        
        print("\nCurrent Balance of ",self.AccName," is : ",self.AccBal)
        print("Deposite Amount is : ",Amount)
        self.AccBal = NewTotal + self.AccBal
        print("Updated Balance of ",self.AccName," is : ",self.AccBal)

    def Withdraw(self,Amount):
        NewTotal = Amount
        if(self.AccBal < Amount or self.AccBal < 0):
            print("Error : Insufficient Balance\n Unable to Withdraw")
        else:
            print("\nCurrent Balance of ",self.AccName," is : ",self.AccBal)
            print("Withdraw Amount is : ",Amount)
            self.AccBal = self.AccBal - NewTotal
            print("Updated Balance of ",self.AccName," is : ",self.AccBal)

    def CalculateIntrest(self):
        Intrest = 0
        Intrest = (self.AccBal * BankAccount.ROI) / 100

        print("\nCurrent Balance of ",self.AccName," is : ",self.AccBal)
        print("Intrest Rate is : ",BankAccount.ROI)
        self.AccBal = self.AccBal + Intrest
        print("Updated Balance of ",self.AccName," is : ",self.AccBal)
        
    
def main():

    obj1 = BankAccount("Omkar Deshmukh",10000)
    obj2 = BankAccount("Mansvi D",20000)
    obj3 = BankAccount("Swara B",15000)
    
    obj1.Display()
    obj2.Display()
    obj3.Display()
    
    obj1.Deposit(500)
    obj1.Withdraw(300)
    obj1.CalculateIntrest()

if __name__ == "__main__":
    main()