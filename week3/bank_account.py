class BankAccount():

    def __init__(self, name, balance, currency):
        if not isinstance(name, str):
            raise TypeError

        if not isinstance(balance, int):
            raise TypeError

        if balance < 0:
            raise ValueError

        if not isinstance(currency, str):
            raise TypeError

        self.__name = name
        self.__balance = balance
        self.__currency = currency
        self.__history = ["Account was created"]

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def get_currency(self):
        return self.__currency

    def get_history(self):
        return self.__history

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(
            self.get_name(), self.get_balance(), self.get_currency())

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.get_balance()

    def deposit(self, ammount):
        self.__balance += ammount
        self.__history.append("Deposited {}{}".format(
            self.get_balance(), self.get_currency()))

    def withdraw(self, amount):
        if amount % 10 != 0:
            raise ValueError("Enter amount that is multiple by 10.")
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            return True
        return False

    def transfer_to(self, account, amount):
        if isinstance(account, BankAccount):
            if self.get_currency() == account.get_currency():
                return True
        else:
            raise TypeError("The given account is not valid.")
        return False

    def history(self):
        return self.get_history()
