import pandas as pd
from scipy.optimize import linprog

df = pd.read_csv('data/ad_spend.csv')
costs = df['cpc'].values
clicks = df['expected_clicks'].values
budget = 10000

res = linprog(c=costs, A_ub=[clicks], b_ub=[budget], method='highs')
print("Optimized spend:", res.x)
