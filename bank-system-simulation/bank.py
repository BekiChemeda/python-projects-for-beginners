import json
import logging
from pathlib import Path
from abc import ABC, abstractmethod


# =========================
# Logging Configuration
# =========================

LOG_FILE = Path(__file__).resolve().parent / "bank.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("BankSystem")


# =========================
# Account Models
# =========================

class Account(ABC):
    def __init__(self, account_number: int, owner: str, balance: float = 0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            logger.error(
                "Invalid deposit amount: %s for account %s",
                amount,
                self.account_number,
            )
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        logger.info(
            "Deposit | Account: %s | Amount: %.2f | New balance: %.2f",
            self.account_number,
            amount,
            self.balance,
        )

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


class SavingsAccount(Account):
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            logger.error(
                "Invalid withdrawal amount: %s for account %s",
                amount,
                self.account_number,
            )
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            logger.error(
                "Insufficient funds | Account: %s | Requested: %.2f | Balance: %.2f",
                self.account_number,
                amount,
                self.balance,
            )
            raise ValueError("Insufficient funds")

        self.balance -= amount
        logger.info(
            "Withdrawal | Account: %s | Amount: %.2f | New balance: %.2f",
            self.account_number,
            amount,
            self.balance,
        )


class CurrentAccount(Account):
    def __init__(
        self,
        account_number: int,
        owner: str,
        balance: float = 0.0,
        overdraft_limit: float = 500.0,
    ):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            logger.error(
                "Invalid withdrawal amount: %s for account %s",
                amount,
                self.account_number,
            )
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance + self.overdraft_limit:
            logger.error(
                "Overdraft exceeded | Account: %s | Requested: %.2f | Balance: %.2f | Limit: %.2f",
                self.account_number,
                amount,
                self.balance,
                self.overdraft_limit,
            )
            raise ValueError("Overdraft limit exceeded")

        self.balance -= amount
        logger.info(
            "Withdrawal | Account: %s | Amount: %.2f | New balance: %.2f",
            self.account_number,
            amount,
            self.balance,
        )


# =========================
# Bank System
# =========================

class Bank:
    DATA_FILE = Path(__file__).resolve().parent / "accounts.json"

    def __init__(self):
        if not self.DATA_FILE.exists():
            self._write_data({})
            logger.info("Initialized new accounts data file")

    def _read_data(self) -> dict:
        with self.DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _write_data(self, data: dict) -> None:
        with self.DATA_FILE.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def _generate_account_number(self) -> int:
        data = self._read_data()
        return max(map(int, data.keys()), default=1000) + 1

    def create_account(self, owner: str, account_type: str) -> int:
        if account_type not in {"savings", "current"}:
            logger.error("Invalid account type attempted: %s", account_type)
            raise ValueError("Invalid account type")

        data = self._read_data()
        account_number = self._generate_account_number()

        data[str(account_number)] = {
            "owner": owner,
            "type": account_type,
            "balance": 0.0,
        }

        self._write_data(data)

        logger.info(
            "Account created | Account: %s | Owner: %s | Type: %s",
            account_number,
            owner,
            account_type,
        )

        return account_number

    def _load_account_object(self, account_number: int) -> Account:
        data = self._read_data()
        record = data.get(str(account_number))

        if not record:
            logger.error("Account not found: %s", account_number)
            raise ValueError("Account not found")

        if record["type"] == "savings":
            return SavingsAccount(
                account_number,
                record["owner"],
                record["balance"],
            )

        return CurrentAccount(
            account_number,
            record["owner"],
            record["balance"],
        )

    def _save_balance(self, account: Account) -> None:
        data = self._read_data()
        data[str(account.account_number)]["balance"] = account.balance
        self._write_data(data)

    def deposit(self, account_number: int, amount: float) -> None:
        account = self._load_account_object(account_number)
        account.deposit(amount)
        self._save_balance(account)

    def withdraw(self, account_number: int, amount: float) -> None:
        account = self._load_account_object(account_number)
        account.withdraw(amount)
        self._save_balance(account)

    def get_account(self, account_number: int) -> dict:
        data = self._read_data()
        account = data.get(str(account_number))

        if not account:
            logger.error("Account lookup failed: %s", account_number)
            raise ValueError("Account not found")

        logger.info("Account retrieved: %s", account_number)

        return {
            "account_number": account_number,
            **account,
        }