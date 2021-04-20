import yfinance as yf
import pandas as pd
import os
import sys

class Loader:

	def __init__(self, interval: str):
		"""
		interval: str
			Временной интревал (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
		"""
		self.interval = interval

	def download(self, ticker: str,  start_date: str, end_date: str):
		"""
		Параметры:

		ticker: str
			Ticker на Yahoo Finance
		start_date: str
			Дата первого наблюдения,
		end_date: str
			Дата последнего наблюдения

		Вывод:

		data: pd.DataFrame
			Данные по указанному тикеру
		"""

		data = yf.Ticker(ticker).history(start=start_date, end=end_date, interval = self.interval )
		data = data.reset_index()
		data['ticker'] = ticker

		return data