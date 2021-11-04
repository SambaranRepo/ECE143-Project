from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://nips.cc/Conferences/2018/Schedule?type=Poster').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('papers_with_abstract.csv', 'a')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['YEAR', 'TITLE', 'Authors', 'Paper Link', 'ABSTRACT'])
count = 0
for section in soup.find_all('div',class_='maincard narrower poster'):
    try: 
        count+=1
        title = section.find('div', class_='maincardBody')
        title_text = title.text
        author = section.find('div',class_='maincardFooter')
        authors = author.text
        link_portion = section.find('div', class_ = '')
        link_portion = link_portion.find_all('span')
        pdf_link = ''
        for links in link_portion: 
            link_a = str(links.a).split('="')
            link_type = links.a.text
            if link_type == ' Paper': 
                pdf_link = link_a[2].split('" title')[0]
        paper = requests.get(pdf_link).text
        paper_soup = BeautifulSoup(paper, 'lxml')
        abstracts = paper_soup.find('div',class_='container-fluid')
        abstracts = abstracts.find('div', class_='col')
        abstract = abstracts.find_all('p')[3].text
        entry = [2018, title_text, authors, pdf_link, abstract]
    except Exception as e:
        entry = ''
    print('Progress : {}'.format(count /(len(soup.find_all('div',class_='maincard narrower poster')))))
    csv_writer.writerow(entry)

    
# section = soup.find('div', class_='maincard narrower poster')
# title = section.find('div', class_='maincardBody')
# title_text = title.text
# author = section.find('div',class_='maincardFooter')
# authors = author.text
# link_portion = section.find('div', class_ = '')
# link_portion = link_portion.find_all('span')
# pdf_link = ''
# for links in link_portion: 
#    link_a = str(links.a).split('="')
#    link_type = links.a.text
#    if link_type == ' Paper': 
#        pdf_link = link_a[2].split('" title')[0]
# paper = requests.get(pdf_link).text
# paper_soup = BeautifulSoup(paper, 'lxml')
# abstracts = paper_soup.find('div',class_='container-fluid')
# abstracts = abstracts.find('div', class_='col')
# abstract = abstracts.find_all('p')[3].text
# print(abstract)
    
   

csv_file.close()