
import os
import json

class Bank:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        self.account_length = 10
        self.initiate_file()
        print(self.generate_account())
        
     #This method initiate accounts.json and settings.json files
    def initiate_file(self):
        if not os.path.exists(os.path.join(os.path.dirname(__file__), 'accounts.json')):
            with open(os.path.join(os.path.dirname(__file__), 'accounts.json'), "w") as f:
                json.dump([],f,indent=4)
        setting = {
        "last_account": 1000
        }
        if not os.path.exists(os.path.join(os.path.dirname(__file__), 'settings.json')):
            with open(os.path.join(os.path.dirname(__file__), 'settings.json'), "w") as f:
                json.dump(setting,f,indent=4)
     
    #This method Loads Account numbers
    def load_accounts(self):
                with open(os.path.join(os.path.dirname(__file__), "accounts.json"), "r") as f:
                    accounts = json.load(f)
                return accounts
                
                
    #   This Method loads the whole setting
    def load_settings(self):
          with open(os.path.join(os.path.dirname(__file__), "settings.json"), "r") as f:
                    setting = json.load(f)
          return setting          
                
                
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
        try:
            setting = self.load_settings()
            return setting['last_account']
        except Exception as e:
            print(f"Error happened while returning last account: {e}")
            
    #This method increments Account Number 
    def increment_acc(self):
        with open(os.path.join(os.path.dirname(__file__), "settings.json"), "r") as f:
                    setting = json.load(f)
        setting['last_account'] += 1
        with open(os.path.join(os.path.dirname(__file__), "settings.json"), "w") as f:
                    json.dump(setting,f,indent=4)
    # This account generates account number
    
    def generate_account(self):
        self.increment_acc()
        return self.last_account()
            
bank = Bank("Beki","Chemeda",18)