import requests
import bs4
import copy
from .FileDetail import FileDetail
from .FileList import FileList


class Sfile():
    def __init__(self):
        self.base_url = 'https://sfile.mobi'
        self.base_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        }

    def search_files(self, query, page=1) -> list[FileList]:
        headers = copy.deepcopy(self.base_headers)
        if page <= 0:
            raise Exception('page must be greater than 0')
        if page > 1:
            page = f'&page={page}'
        else:
            page = ''
        res = requests.get(
            f'{self.base_url}/search.php?q={query}' + page, headers=headers)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        list = soup.find_all('div', class_='list', limit=20)
        files = []
        for file in list:
            files.append(
                FileList(file.find('a').contents[0], '0', file.find('a').get('href')),)

        return files

    def latest_upload(self, page=1) -> list[FileDetail]:
        headers = copy.deepcopy(self.base_headers)
        if page <= 0:
            raise Exception('page must be greater than 0')
        if page > 1:
            page = f'?page={page}'
        else:
            page = ''
        res = requests.get(
            f'{self.base_url}/uploads.php' + page, headers=headers)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        list = soup.find_all('div', class_='list', limit=20)
        files = []
        for file in list:
            files.append(
                FileList(file.find('a').contents[0], '0', file.find('a').get('href')),)

        return files

    def trending_files(self, page=1) -> list[FileDetail]:
        headers = copy.deepcopy(self.base_headers)
        if page <= 0:
            raise Exception('page must be greater than 0')
        if page > 1:
            page = f'?page={page}'
        else:
            page = ''
        res = requests.get(
            f'{self.base_url}/top.php' + page, headers=headers)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        list = soup.find_all('div', class_='list', limit=20)
        files = []
        for file in list:
            files.append(
                FileList(file.find('a').contents[0], '0', file.find('a').get('href')),)

        return files

    def get_detail(self, url):
        if not url:
            raise Exception('url is required')
        return FileDetail(url)
