from pytrends.request import TrendReq
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
pytrends = TrendReq()
pytrends.build_payload(["Maharashtra"], timeframe='now 7-d')
trending_data = pytrends.interest_over_time()
print(trending_data.head())

