from bs4 import BeautifulSoup
import requests
import csv
from tqdm import tqdm

icml_links = ['https://icml.cc/Conferences/2018/Schedule?type=Poster','https://icml.cc/Conferences/2019/Schedule?type=Poster','https://icml.cc/Conferences/2020/Schedule?type=Poster']

parent = '/home/sambaran/UCSD/Quarter2/ECE143/Project/data'
csv_file = open(parent + '/icml_2018-2020.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['YEAR', 'TITLE', 'Authors', 'Paper Link', 'ABSTRACT'])

for icml in tqdm(icml_links):
    year = icml.split('/')[4]
    source = requests.get(icml).text
    soup = BeautifulSoup(source, 'lxml')
    for section in tqdm(soup.find_all('div', class_='maincard narrower Poster')): 
        try:
            a= str(section).split('\n')
            id = a[0].split('card_')[1].split('">')[0]
            title = str(section.find('div',class_='maincardBody').text)
            authors = str(section.find('div',class_='maincardFooter').text)
            authors = authors.replace(' ·', ',')
            link = 'https://icml.cc/Conferences/2020/Schedule?showEvent=' + id

            pdf_source = requests.get(link).text
            pdf_soup = BeautifulSoup(pdf_source, 'lxml')
            abstract = pdf_soup.find('div', class_='abstractContainer').text
            entry = [year,title, authors, link,abstract]
        except Exception as e:
            entry = ''
        csv_writer.writerow(entry)

csv_file.close()