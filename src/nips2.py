from bs4 import BeautifulSoup
import requests
import csv
from tqdm import tqdm

nips_links = ['https://nips.cc/Conferences/2016/Schedule?type=Poster','https://nips.cc/Conferences/2017/Schedule?type=Poster',\
    'https://nips.cc/Conferences/2018/Schedule?type=Poster','https://nips.cc/Conferences/2019/Schedule?type=Poster',\
        'https://nips.cc/Conferences/2020/Schedule?type=Poster']

parent = '/home/sambaran/UCSD/Quarter2/ECE143/Project/data'
csv_file = open(parent + '/nips_2018-2020.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['YEAR', 'TITLE', 'Authors', 'Paper Link', 'ABSTRACT', 'Affiliations'])

for nips in tqdm(nips_links):
    year = nips.split('/')[4]
    source = requests.get(nips).text
    soup = BeautifulSoup(source, 'lxml')

    for section in tqdm(soup.find_all('div', class_='maincard narrower poster')): 
        try:
            a= str(section).split('\n')
            id = a[0].split('card_')[1].split('">')[0]
            title = str(section.find('div',class_='maincardBody').text)
            authors = str(section.find('div',class_='maincardFooter').text)
            authors = authors.replace(' ·', ',')
            link = f'https://nips.cc/Conferences/{year}/Schedule?showEvent=' + id
            pdf_source = requests.get(link).text
            pdf_soup = BeautifulSoup(pdf_source, 'lxml')
            abstract = pdf_soup.find('div', class_='abstractContainer').text
            author_link = pdf_soup.find_all('button', class_ = 'btn btn-default')
            affiliations = []
            for item in author_link: 
                author_id  = str(item).split("Speaker('")[1].split("')")[0]
                # print(author_id)
                auth_profile_link = f"https://nips.cc/Conferences/{year}/Schedule?showSpeaker={author_id}"
                auth_page = requests.get(auth_profile_link).text
                auth_soup = BeautifulSoup(auth_page, 'lxml')
                name = auth_soup.find('div' , class_ = 'maincard Remark col-sm-12').h4.text
                # print(name)
                affiliations.append(name)
            entry = [year,title, authors, link,abstract, affiliations]
        except Exception as e:
            entry = ''
        csv_writer.writerow(entry)

csv_file.close()