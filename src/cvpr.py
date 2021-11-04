from bs4 import BeautifulSoup
import requests
import csv
from tqdm import tqdm

cvpr_links = ['https://openaccess.thecvf.com/CVPR2018?day=2018-06-19','https://openaccess.thecvf.com/CVPR2018?day=2018-06-20',\
    'https://openaccess.thecvf.com/CVPR2018?day=2018-06-21', 'https://openaccess.thecvf.com/CVPR2019?day=2019-06-18', \
    'https://openaccess.thecvf.com/CVPR2019?day=2019-06-19','https://openaccess.thecvf.com/CVPR2019?day=2019-06-20',\
    'https://openaccess.thecvf.com/CVPR2020?day=2020-06-16','https://openaccess.thecvf.com/CVPR2020?day=2020-06-17',\
    'https://openaccess.thecvf.com/CVPR2020?day=2020-06-18']
csv_file = open('cvpr_2018-2020.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['YEAR', 'TITLE', 'Authors', 'Paper Link', 'ABSTRACT'])

for cvpr in tqdm(cvpr_links): 
    source = requests.get(cvpr).text
    soup = BeautifulSoup(source, 'lxml')
    year = cvpr[-10:-6]
    count = 0
    title_list = soup.find_all('dt', class_='ptitle')
    for title in tqdm(title_list): 
        count +=1
        title_entry = title.a.text
        link = str(title.a).split('href="')
        link = link[1].split('">')
        link_cvpr = 'https://openaccess.thecvf.com/' + link[0]
        pdf_source = requests.get(link_cvpr).text
        pdf_soup = BeautifulSoup(pdf_source, 'lxml')
        authors = pdf_soup.find('i').text
        abstract = pdf_soup.find('div', id='abstract').text
        csv_writer.writerow([year, title_entry,authors, link_cvpr, abstract])

csv_file.close()
        

        

