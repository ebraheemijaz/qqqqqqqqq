import pandas as pd                        
from pytrends.request import TrendReq
from time import sleep
import random

keywords = [
    "why",
    "what",
    "how"
]

for keyword in keywords:
    print(f"Searching keyword '{keyword}' pash 1 hour")
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword], timeframe='now 1-H')
    related_queries = pytrend.related_queries()
    related_queries[keyword]['rising'].to_csv(f"{keyword}.csv")
    sleep(random.randint(3,9))