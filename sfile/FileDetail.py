import requests
import bs4
import re
from .SfileException import LockedFileException, FileNotFoundException


class FileDetail():
    def __init__(self, url):
        self.__base_headers = {
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
        self.url = url
        self._get_detail()

    def _get_detail(self):
        session = requests.Session()
        res = session.get(self.url, headers=self.__base_headers)
        if res.status_code == 404:
            raise FileNotFoundException()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        div_list = soup.findAll('div', class_='list')
        self.name = soup.find('h1').contents[0]
        self.date = div_list[2].contents[-1]
        self.download_count = div_list[3].contents[-1][-1]
        # get download link
        dl = soup.find('a', id='download').get('href')
        if not dl:
            raise LockedFileException()
        res2 = session.get(dl, headers=self.__base_headers)
        soup = bs4.BeautifulSoup(res2.text, 'html.parser')
        href = soup.find('a', id='download').get('href')
        k = soup.find('a', id='download').get('onclick')
        self.download_link = f"{href}?k={re.search('[a-f0-9]{32}', k).group()}"
        self.size = re.search('(?<=Download File )\(.*?\)',
                              soup.find('a', id='download').contents[-1]).group()
        return
