import requests
from bs4 import BeautifulSoup
import re  # 정규식 사용
from pandas import DataFrame


class Crawling():
    @staticmethod
    def summoner_names(soup, top_player_num=10) -> list:
        ranker_table = soup.find_all('table', {'class': 'table table-page-1 table-sort-tier'})
        col_names = ranker_table[0].find_all('th')
        # print(col_names)
        # print(len(col_names)) # 9
        # Rank, Name, Tier, LP, WinRate, TOP4 %, Played, Wins, TOP4
        for col_name in col_names:
            print(col_name.text.strip())  # 9 column headers
        print("--" * 20)
        # find summoner names
        summoners = ranker_table[0].find_all('td', {'class': "summoner"})
        print(type(summoners))
        print(len(summoners))

         # analyze given number of top players
        top_players = []
        for i in range(top_player_num):
            top_players.append(summoners[i].text[5:].strip())
        # print(top_players)  # get player names
        return top_players

    @staticmethod
    def access_website(self, url, *args):
        # user agent
        if args:
            for name in args:

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
        res = requests.get(url, headers=headers)
        res.raise_for_status()  # 혹시 문제가 있을시 에러)
        soup = BeautifulSoup(res.text, 'lxml')
        return soup

    @staticmethod
    def analyze_summoner(self, summoners: list):
        print(summoners)


if __name__ == '__main__':
    crawl = Crawling()
    url = "https://lolchess.gg/leaderboards"
    soup = crawl.access_website(url)  # access the website
    names = crawl.summoner_names(soup, 10)  # get summoner names
    url = "https://lolchess.gg/profile/kr/"

    crawl.analyze_summoner(names)