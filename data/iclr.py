from bs4 import BeautifulSoup
import requests
import csv
from tqdm import tqdm

iclr_links = ["https://iclr.cc/Conferences/2018/Schedule?type=Poster","https://iclr.cc/Conferences/2019/Schedule?type=Poster","https://iclr.cc/Conferences/2020/Schedule?type=Poster"]    
csv_file = open('iclr_2018-2019.csv', 'w' , encoding="utf-8")


csv_writer = csv.writer(csv_file)
csv_writer.writerow(['YEAR', 'TITLE', 'AUTHORS', 'PAPER LINK', 'ABSTRACT'])

for iclr in tqdm(iclr_links): 
    year = iclr.split('/')[4]
    source = requests.get(iclr).text
    soup = BeautifulSoup(source, 'lxml')
    for section in tqdm(soup.find_all('div', class_='maincard narrower poster')): 
        try:
            a= str(section).split('\n')
            id = a[0].split('card_')[1].split('">')[0]
            title = str(section.find('div',class_='maincardBody').text)
            authors = str(section.find('div',class_='maincardFooter').text)
            authors = authors.replace(' ·', ',')
            if (iclr == 'https://iclr.cc/Conferences/2018/Schedule?type=Poster'):
                link = 'https://iclr.cc/Conferences/2018/Schedule?showEvent=' + id
            elif (iclr == 'https://iclr.cc/Conferences/2019/Schedule?type=Poster'):
                link = 'https://iclr.cc/Conferences/2019/Schedule?showEvent=' + id
            elif (iclr == 'https://iclr.cc/Conferences/2020/Schedule?type=Poster'):
                link = 'https://iclr.cc/Conferences/2020/Schedule?showEvent=' + id
            pdf_source = requests.get(link).text
            pdf_soup = BeautifulSoup(pdf_source, 'lxml')
            abstract = pdf_soup.find('div', class_='abstractContainer').text
            entry = [year,title, authors, link,abstract]
        except Exception as e:
            entry = ''
        csv_writer.writerow(entry)

csv_file.close()