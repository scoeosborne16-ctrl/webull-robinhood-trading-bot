import numpy as np
import pandas as pd

class RSIMACD:
    def __init__(self, rsi_period=14, macd_fast=12, macd_slow=26, macd_signal=9):
        self.rsi_period = rsi_period
        self.macd_fast = macd_fast
        self.macd_slow = macd_slow
        self.macd_signal = macd_signal

    def calculate_rsi(self, prices):
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=self.rsi_period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=self.rsi_period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_macd(self, prices):
        exp1 = prices.ewm(span=self.macd_fast, adjust=False).mean()
        exp2 = prices.ewm(span=self.macd_slow, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=self.macd_signal, adjust=False).mean()
        return macd, signal

    def generate_signals(self, prices):
        rsi = self.calculate_rsi(prices)
        macd, signal = self.calculate_macd(prices)
        buy_signal = (rsi < 30) & (macd > signal)
        sell_signal = (rsi > 70) & (macd < signal)
        return buy_signal, sell_signal

# Example Usage:
# strategy = RSIMACD()
# buy, sell = strategy.generate_signals(price_data)