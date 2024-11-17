# Sfile Web Scraper

Python3 library for scraping files from [Sfile.mobi](https://sfile.mobi).
**This project is not affiliated with Sfile.mobi in any way.**

## Installation

```sh
pip3 install git+ssh://git@github.com/dianudi/sfile-scraper.git
```

## Usage

```python
from sfile import Sfile

s = Sfile()

# get latest uoload files on page 1
files = s.latest_upload()
for file in files:
    file_detail = file.get_detail()
    print(f'Name: {file_detail.name}\n Size: {file_detail.size}\n Uploaded: {file_detail.date}\n Downloaded: {file_detail.download_count}\n Direct Download Link: ${file_detail.download_link}')

# get trending files on page 2
files = s.trending_files(page=2)

# search files
files = s.search_files('python')

# get detail of file by given link
file = s.get_detail('https://sfile.mobi/xxxxxx')
print(f'Name: {file.name}\n Size: {file.size}\n Uploaded: {file.date}\n Downloaded: {file.download_count}\n Direct Download Link: ${file.download_link}')

```

## Disclaimer

If you use this API, you also bound to the terms of usage of their website
