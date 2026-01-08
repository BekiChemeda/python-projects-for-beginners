
import os
import json
from pathlib import Path

class Bank:
    BASE_DIR = Path(__file__).resolve().parent
    ACCOUNTS_FILE = BASE_DIR / "accounts.json"
    SETTINGS_FILE = BASE_DIR / "settings.json"
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self._initialize_files()

    def _initialize_files(self) -> None:
        if not self.ACCOUNTS_FILE.exists():
            self._write_json(self.ACCOUNTS_FILE, [])

        if not self.SETTINGS_FILE.exists():
            self._write_json(self.SETTINGS_FILE, {"last_account": 1000})

    # JSON Utilities 

    @staticmethod
    def _read_json(path: Path):
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def _write_json(path: Path, data) -> None:
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        
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
    def save_account(self):
        full_name = self.first + self.last
        account_number = self.generate_account()
        
bank = Bank("Beki","Chemeda",18)