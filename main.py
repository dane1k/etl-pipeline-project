import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

db_url = "postgresql://postgres:danekNZsukableat2004-@localhost:5432/stocks_db"
engine = create_engine(db_url)

try:
    with engine.connect() as connection:
        print("Connected!")
except Exception as e:
    print("Didnt connect TnT :", e)

symbols = ['BTC-USD', '^GSPC', 'ETH-USD']
for symbol in symbols:
    stock = yf.Ticker(symbol)
    data = stock.history(period="1mo")
    data.reset_index(inplace=True)
    data.rename(columns={"Date": "date"}, inplace=True)
    data['symbol'] = symbol
    data['name'] = stock.info.get('longName')

    data.to_sql("stocks_data", engine, if_exists="append", index=False)
    print(f"Data for {symbol} has been added to stocks_data")

# testing
df = pd.read_sql("SELECT * FROM stocks_data", engine)
print(f"\n \n \n \n {df.head()}")
