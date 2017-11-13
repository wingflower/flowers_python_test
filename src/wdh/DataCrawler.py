#-*- coding : utf-8 -*-
"""
    Author : Flower
    Time attack
        2017.11.13 ~
    Start log
        2017.11.13  [start]
"""
import requests
from bs4 import BeautifulSoup as bs


class DataCrawler():
    def __init__(self):
        pass

    def crawler(self, url):
        source_code = requests.get(url).text
        html_rs = bs(source_code, 'lxml')

    def run(self):
        pass


if __name__ == '__main__':
    DC = DataCrawler()
    DC.run()
