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


stock = yf.Ticker("AAPL")
data = stock.history(period="1mo")
data.reset_index(inplace=True)
data.rename(columns={"Date": "date"}, inplace=True)

data.to_sql("stocks_data", engine, if_exists="replace", index=False)
print("Data has been transfered to stocks_data")

df = pd.read_sql("SELECT * FROM stocks_data", engine)
print(df.head())