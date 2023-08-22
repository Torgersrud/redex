from CRYPTOPRICETRACKER import getCoinData
from redbot import get_reddit_thread, textCount
from cleanfile import frequentWords


cryptodata = getCoinData()

tokens = [x for x in cryptodata.keys()]
marketcap = [x for x in cryptodata.values()]

subreddits = ["CryptoCurrency", "Crypto", "bitcoin", "btc", "cryptomarkets", "bitcoinbeginners", "cryptocurrencies", "altcoin", 
              "cryptocurrencytrading", "crypto_general", "ico", "dogecoin", "ripple", "litecoin", "monero", "stellar", "binance", 
              "coinbase", "ledgerwallet", "defi"]
              

corpus = "\n".join([get_reddit_thread(i) for i in subreddits])

countedTokens = textCount(tokens, corpus)

collectedData = zip(tokens, marketcap, countedTokens.values())
for i in collectedData:
    if i[-2] == 0:
        continue
    print(i)