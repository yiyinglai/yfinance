import yfinance as yf
import pandas as pd
import argparse
import traceback

# tickers =["ANET","ASML","CMI","CAT","NEE","PYPL","MAR","BSX","CCL","002050.sz","002851.sz","603816.ss","603399.ss","002937.SZ","603339.ss","0189.hk","603345.ss","605060.ss","600481.ss","002518.sz","601567.ss","000682.SZ","603191.ss","000400.sz","601877.ss","300910.sz","600089.ss","002850.sz","300041.sz","603871.ss","002714.sz","002895.sz","603309.ss","603127.ss","603676.ss","000739.sz","603279.ss","300724.sz","300763.sz","300316.sz","600438.ss","002129.sz","601012.ss","002459.sz"]
tickers =["ANET"]
print('tickers:', tickers)

# create an empty dataframe to store the results
results = pd.DataFrame()

for ticker in tickers:
    attempt = 1  # initialize attempt counter
    while True:
        try:
            print(f"Attempt {attempt} for {ticker}")
            # download the data for the ticker
            df = yf.download(ticker, start="2023-01-01", end="2023-07-30", threads=True, proxy="http://127.0.0.1:8001")
            print("df:", df)

            # resample the data by month start
            ms_adj = df.resample("MS").first()
            print(ms_adj)

            # add the resampled data to the results dataframe
            results[ticker] = ms_adj['Adj Close']
            break  # if the download was successful, break the while loop and move to the next ticker
        except Exception as e:
            print(f"An error occurred: {e}. Retrying...")
            traceback.print_exc()
            quit()
            # continue  # if an error occurred, skip the rest of the loop and retry

# save the results dataframe as an Excel file in the current directory
results.to_excel('results.xlsx', index=True)

print(results)
