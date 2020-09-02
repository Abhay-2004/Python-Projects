import yfinance as yt

tickerSymbol = 'GOOGl'

tickerData = yt.Ticker(tickerSymbol)

ticketDf = tickerData.history(period='1d', start = '2020-9-1', end = '2020-9-2')

print(ticketDf)