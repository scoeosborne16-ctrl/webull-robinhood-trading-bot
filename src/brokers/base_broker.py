from abc import ABC, abstractmethod

class BaseBroker(ABC):
    @abstractmethod
    def buy(self, symbol, quantity):
        pass

    @abstractmethod
    def sell(self, symbol, quantity):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_portfolio(self):
        pass
