def ohlcv(df,col):

	df = df.copy()
	df = df[['datetime',col]]
	return df