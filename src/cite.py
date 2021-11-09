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
API_KEY = 'dc1177b38a1f6436bde8972d85643216'
proxies = {
  'http': f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',
}


_AUTHPAGE = 'https://scholar.google.com/citations?user={}&hl=en&oi=ao'

csv_file1 = open('data/nips_affiliations.csv', 'a')
csv_file2 = open('data/nips_citations.csv', 'a')
csv_writer1 = csv.writer(csv_file1)
csv_writer2 = csv.writer(csv_file2)
# csv_writer1.writerow(['year','paper','affiliations'])
# csv_writer2.writerow(['year','paper', 'citations'])

def load_csv():
    data = pd.read_csv('data/nips_2018-2020.csv')
    return data

def author_paper_citations(year, praw , df, adata, pname, i):
    source = requests.get(_AUTHPAGE.format((adata['scholar_id'])), proxies=proxies, verify= False).text
    soup = BeautifulSoup(source, 'lxml')
    updated = False
    google_scholar = soup.find_all('tr', attrs={"class":"gsc_a_tr"})
    for t in (google_scholar):
        cname = t.find('a', attrs={"class":"gsc_a_at"}).text.strip().lower().replace(" ","")
        if cname == pname:
            try:
                cites = t.find('a', attrs={"class":"gsc_a_ac gs_ibl"}).text.strip()
                if cites == "":
                    cites = 0
                else:
                    cites = int(cites)
                csv_writer2.writerow([year , praw, cites])
                csv_writer1.writerow([year , praw, adata['affiliation']])
                updated = True
            except Exception as e:
                pass
            break
    return updated

def get_affiliation(data): 
    for i in tqdm(range(534 + 371 + 1885,len(data))): 
        praw = str(data['TITLE'][i])
        year = data['YEAR'][i]
        pname = praw.lower().replace(" ", "")
        authors = data['Authors'][i].split(', ')
        authors = authors[:1]
        for author in (authors): 
            try:
                adata = next(scholarly.search_author(author.lower()))
                updated = author_paper_citations(year, praw , data, adata, pname, i)
            except StopIteration:
                continue
            if updated: 
                break
    csv_file1.close()
    csv_file2.close()
    return 1


if __name__ == '__main__':
    pg = ProxyGenerator()
    success = pg.ScraperAPI('dc1177b38a1f6436bde8972d85643216')   
    scholarly.use_proxy(pg)
    data = load_csv()
    get_affiliation(data = data)


    