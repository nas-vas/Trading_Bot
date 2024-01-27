import alpaca_trade_api as alpaca
import pandas as pd

api = alpaca.REST('PKDC8TYPG7288KG1VNBJ', 'pGYDEA2MLqdx2I5rvhubmdxuRDjwsdAQZVjUIa5z', 'https://paper-api.alpaca.markets')

active_assets = api.list_assets(status='active') 

# Create a DataFrame
data = {'Symbol': [asset.symbol for asset in active_assets],
        'Name': [asset.name for asset in active_assets]}

df = pd.DataFrame(data)

# Save to Excel
df.to_excel('active_assets.xlsx', index=False)
