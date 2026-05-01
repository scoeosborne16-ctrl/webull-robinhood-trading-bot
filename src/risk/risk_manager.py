# risk_manager.py

class RiskManager:
    def __init__(self, account_balance, risk_per_trade):
        self.account_balance = account_balance
        self.risk_per_trade = risk_per_trade

    def position_size(self, stop_loss_distance):
        if stop_loss_distance <= 0:
            raise ValueError("Stop loss distance must be greater than 0")
        position_size = (self.account_balance * self.risk_per_trade) / stop_loss_distance
        return position_size

    def stop_loss(self, entry_price, position_size, stop_loss_percentage):
        if stop_loss_percentage <= 0:
            raise ValueError("Stop loss percentage must be greater than 0")
        stop_loss_amount = entry_price * (stop_loss_percentage / 100)
        return entry_price - stop_loss_amount

    def validate_risk(self, position_size, stop_loss_distance):
        if position_size <= 0 or stop_loss_distance <= 0:
            return False
        return True

# Example usage:
# risk_manager = RiskManager(account_balance=10000, risk_per_trade=0.02)
# size = risk_manager.position_size(stop_loss_distance=1)
# stop_loss_price = risk_manager.stop_loss(entry_price=100, position_size=size, stop_loss_percentage=1)
# is_valid = risk_manager.validate_risk(size, 1)