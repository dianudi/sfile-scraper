from setuptools import find_packages, setup

setup(
    name='sfile',
    packages=find_packages(exclude=['tests', 'assets']),
    version='0.0.1',
    description='Sfile web scaper',
    author='Dianudi',
    url="https://github.com/dianudi/sfile-scraper",
    keywords=["sfile", "sfile-scraper", "web-scraper", "file-sharing"],
    license='MIT',
    requires=['requests', 'bs4', 'brotli'],
)
