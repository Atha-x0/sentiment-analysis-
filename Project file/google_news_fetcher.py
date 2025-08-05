from GoogleNews import GoogleNews
import sys
import os

os.system('chcp 65001')
sys.stdout.reconfigure(encoding='utf-8')

googlenews = GoogleNews(period='7d')
googlenews.search("Wardha")
results = googlenews.results()

for news in results:
    print(news['title'])
