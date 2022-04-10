class Atm():

    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    def withdrawal(self,cardNumber):
        print("Draw 100 dollars")

    def deposit(self,cardNumber):
        print("Deposit 50 dollars")

    def balance(self,cardNumber):
        print("Your current balance is 1000 dollars")

card=Atm(3094521345,7503)
print(card.withdrawal(100))

    

