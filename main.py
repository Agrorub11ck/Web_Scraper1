import requests
import string
import os
from bs4 import BeautifulSoup


def title_formatting(title):
    translator = str.maketrans('', '', string.punctuation)
    title = str(title.translate(translator))
    return '_'.join(title.split()) + '.txt'


def user_request(number, article):
    for i in range(1, number + 1):
        current_directory = os.getcwd()
        folder_name = 'Page_' + str(i)
        folder_path = os.path.join(current_directory, folder_name)
        os.mkdir(folder_path)
        url = 'https://www.nature.com/nature/articles'
        params = {'searchType': 'journalSearch', 'sort': 'PubDate', 'year': '2020','page': str(i)}
        r = requests.get(url, params=params)
        soup = BeautifulSoup(r.content, 'html.parser')
        for li in soup.find_all('li', class_='app-article-list-row__item'):
            type = li.find('span', class_='c-meta__type').text
            if type == article:
                resource = li.a.get('href')
                r = requests.get('https://www.nature.com' + resource)
                article_soup = BeautifulSoup(r.content, 'html.parser')
                title = title_formatting(article_soup.h1.text.strip())
                print(title)
                article_body = article_soup.find('div', {'class': "c-article-body"})
                if article_body is not None:
                    with open(f'{folder_path}/{title}', 'w', encoding='UTF-8') as f:
                        f.write(article_body.text.strip())


number_of_pages = int(input())
article_type = input()
user_request(number_of_pages, article_type)
