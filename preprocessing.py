import pandas as pd


class Preprocessor:

    def __init__(self, column_name: str):
        """

		:param column_name: str
			Название колонки, которая выбрана для анализа (Open, Close, High, Low)
		"""
        self.col_name = column_name

    def addStatistics(self, df: pd.DataFrame, n: int):
        """

		:param df: pd.DataFrame
			Исходный датафрейм, содержащий столбцы Дата и column_name
		:param n: int
			Длина окна для скользящих статистик
		:return:
		df: pd.DataFrame
			датафрейм с внедренными статистиками
		"""

        df['rolling_mean'] = df[self.col_name].rolling(n).mean()
        df['return'] = df[self.col_name].pct_change().fillna(0)
        df['cumulative_return'] = (df['return'] + 1).cumprod().fillna(0)
        # df['return'] = (pd.Series(["{0:.2f}%".format(val * 100) for
        # 						   val in df['return']], index=df.index))
        # df['cumulative_return'] = (pd.Series(["{0:.2f}%".format(val * 100) for
        #                                       val in df['cumulative_return']], index=df.index))
        return df
