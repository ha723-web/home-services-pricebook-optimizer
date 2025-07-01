# price_optimizer.py

import pandas as pd

def load_data(path='data/home_services_data.csv'):
    df = pd.read_csv(path)
    df['Total Cost'] = df['Labor Cost'] + df['Material Cost']
    df['Profit Margin (%)'] = round(((df['Price'] - df['Total Cost']) / df['Price']) * 100, 2)
    return df

def suggest_price(row, margin_goal=50):
    cost = row['Total Cost']
    target_price = cost / (1 - (margin_goal / 100))
    return round(target_price, 2)

def apply_margin_strategy(df, margin_goal=50):
    df['Suggested Price'] = df.apply(lambda row: suggest_price(row, margin_goal), axis=1)
    return df
