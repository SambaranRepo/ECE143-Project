import numpy as np
from scholarly import scholarly, ProxyGenerator
from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm
import csv
import concurrent.futures
import urllib3
urllib3.disable_warnings()
API_KEY = '4b0b8dca0b014234fcc934501e0960a2'
proxies = {
  'http': f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',
}

csv_file2 = open('data/cvpr_citations.csv', 'w')
csv_writer2 = csv.writer(csv_file2)
# csv_writer1.writerow(['year','paper','affiliations'])
csv_writer2.writerow(['year','paper', 'citations'])

def load_csv():
    data = pd.read_csv('data/cvpr_16-21.csv')
    return data


def get_citations(data): 
    for i in tqdm(range(3000,len(data))): 
        praw = str(data['TITLE'][i])
        year = data['YEAR'][i]
        try:
            adata = scholarly.search_pubs(praw)
            adata = next(adata)
            citations = adata['num_citations']
            csv_writer2.writerow([year, praw, citations])
        except Exception as e: 
            pass
    csv_file2.close()
    return 1


if __name__ == '__main__':
    pg = ProxyGenerator()
    success = pg.ScraperAPI('4b0b8dca0b014234fcc934501e0960a2')   
    scholarly.use_proxy(pg)
    data = load_csv()
    get_citations(data = data)


    