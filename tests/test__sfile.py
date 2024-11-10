import unittest
from sfile import Sfile, SfileException


class TestSfile(unittest.TestCase):

    def test_search_files(self):
        sfile = Sfile()
        files = sfile.search_files('python')
        self.assertTrue(files)

        # test with page
        files = sfile.search_files('python', 2)
        self.assertTrue(files)

    def test_latest_upload(self):
        sfile = Sfile()
        files = sfile.latest_upload()
        self.assertTrue(files)

        # test with page
        files = sfile.latest_upload(2)
        self.assertTrue(files)

    def test_trending_files(self):
        sfile = Sfile()
        files = sfile.trending_files()
        self.assertTrue(files)

        # test with page
        files = sfile.trending_files(2)
        self.assertTrue(files)

    def test_get_detail(self):
        sfile = Sfile()
        files = sfile.latest_upload()
        if not files:
            raise Exception('No files found')
        file = sfile.get_detail(files[0].url)
        self.assertTrue(file.name)
        self.assertTrue(file.size)
        self.assertTrue(file.download_count)
        self.assertTrue(file.download_link)

        # test with invalid url
        self.assertRaises(SfileException.FileNotFoundException,
                          sfile.get_detail, 'https://sfile.mobi/invalid')
