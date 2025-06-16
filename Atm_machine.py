class ATM:

    def __init__(self):
        
        self.__balance = 0
        self.__pin = 0
        self.Menu()
    def Menu(self):
        USER_INPUT =input(
            """ HOW WOULD YOU LIKE TO PROCEED!
                    1. Create A New PIN                
                    2. Deposit  Cash
                    3. Withdraw Cash
                    4. Check Balance 
                    5.EXIT    
"""
        )

        if USER_INPUT == "1":
          print ("CREATE PIN")
          self.Create_pin()
        elif USER_INPUT == "2":
          self.Cash_DEPOSIT()
        elif USER_INPUT == "3":
          self.Withdraw()
        elif USER_INPUT == "4":
          self.balance
        elif USER_INPUT == "5":
          print("BYE! THANKYOU FOR USING ATM ")
          self.EXIT()
        else:
           print(" INVALID SELECTION")

          
              
    def Create_pin(self):
        pin = int(input("ENTER PIN CODE "))
        self.pin += pin
        print ("PIN SET")
    def Cash_DEPOSIT(self):
        pin = int(input("ENETR PIN CODE "))
        if pin == self.pin:
            amount = int(input("ENTER AMOUNT "))
            self.balance += amount
            print(f"{amount} ADDED SUCESSFULLY")
            print(f" YOUR Balance is  {self.balance}")
        else:
           print("INVALID PIN! Check PIN AND TRY AGAIN")
           
    def Withdraw(self): 
        pin =int( input("ENETR PIN CODE "))
        if pin == self.pin:
            amount = int(input("ENTER AMOUNT"))
            if amount < self.balance:
             print ("insufficent Funds")
            else:
                self.balance -= amount
                print(f" YOUR Balance is  {self.balance}")
        else:
              print("INVALID PIN! Check PIN AND TRY AGAIN")
           
    def CHK_Balance(self):
        pin =int( input("ENETR PIN CODE "))
        if pin == self.pin:
            print(f" YOUR Balance is  {self.balance}")
        else:
           print("INVALID PIN! Check PIN AND TRY AGAIN")
           
    
    def EXIT(self):
       SystemExit

