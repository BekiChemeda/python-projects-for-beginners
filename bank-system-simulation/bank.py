#pylint:disable=E1101
#pylint:disable=E0601
import os
import json
import random

class Bank:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        self.account_length = 10
        self.initiate_file()
        print(self.generate_account())
        
     #This method initiate files   
    def initiate_file(self):
        if not os.path.exists(os.path.join(os.path.dirname(__file__), 'accounts.json')):
            with open(os.path.join(os.path.dirname(__file__), 'accounts.json'), "w") as f:
                json.dump([],f,indent=4)
     
    #This method Loads Account numbers
    def load_accounts(self):
                with open(os.path.join(os.path.dirname(__file__), "accounts.json"), "r") as f:
                    accounts = json.load(f)
                return accounts
                     
    # This method checks if the generated account number is unique 
         
    def is_unique(self,account):
        accounts = self.load_accounts()
        if accounts:
            for a in accounts:
                if a['account_number'] == account:
                    return False
        return True
    
    # This method returns the last account number 
    
    def last_account(self):
        if not os.path.exists(os.path.join(os.path.dirname(__file__), 'settings.json')):
            with open(os.path.join(os.path.dirname(__file__), 'settings.json'), "w") as f:
                f.write
    # This account generates account number
    
    def generate_account(self):
        account_number=[]
        for a in range(self.account_length):
            account_number.append(str(random.randint(0,9)))
        account_number = "".join(account_number)
        return account_number
            
bank = Bank("Beki","Chemeda",18)