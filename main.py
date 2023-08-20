from CRYPTOPRICETRACKER import getCoinData
from redbot import get_reddit_thread, textCount
from cleanfile import frequentWords


cryptodata = getCoinData()

tokens = [x for x in cryptodata.keys()]
marketcap = [x for x in cryptodata.values()]

subreddits = ["CryptoCurrency", "Crypto"]

corpus = "".join([get_reddit_thread(i) for i in subreddits])

countedTokens = textCount(tokens, corpus)