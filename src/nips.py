from bs4 import BeautifulSoup
import requests
import csv
from tqdm import tqdm
nips = ['https://papers.nips.cc/paper/2018','https://papers.nips.cc/paper/2019','https://papers.nips.cc/paper/2020',]


parent = '/home/sambaran/UCSD/Quarter2/ECE143/Project/data'
csv_file = open(parent + '/nips_2018-2020.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['YEAR', 'TITLE', 'Authors', 'Paper Link', 'ABSTRACT'])

for nips_links in tqdm(nips):
    source = requests.get(nips_links).text
    soup = BeautifulSoup(source, 'lxml')
    year = nips_links[-4:]
    section = soup.find('div', class_ = 'col')
    section = section.ul
    exceptions = 0
    for papers in tqdm(section.find_all('li')): 
        try:
            author = papers.i.text
            link_str = str(papers.a)
            title = papers.a.text
            link = link_str.split('href="')
            link = link[1]
            link = 'https://papers.nips.cc/' + link.split('">')[0]
            pdf = requests.get(link).text
            pdf_soup = BeautifulSoup(pdf, 'lxml')
            abstract_section = pdf_soup.find('div',class_='col')
            abstract = abstract_section.find_all('p')[3].text
            entry = [year, title, author, link, abstract]
        except Exception as e:
            entry = ['']
            exceptions +=1
        csv_writer.writerow(entry)
print('Number of exceptions: {}'.format(exceptions))
csv_file.close()