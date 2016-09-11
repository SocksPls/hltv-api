import requests
import json
from bs4 import BeautifulSoup


def get_parsed_page(url):
    return BeautifulSoup(requests.get(url).text, "lxml")


def top5teams():
    home = get_parsed_page("http://hltv.org/")
    count = 0
    teams = []
    for team in home.find_all("div", {"class": "vsbox", })[:5]:
        count += 1
        teamname = team.find_all("div")[2].text.strip()
        teams.append(teamname)
    return teams


def getmatches():
    matches = get_parsed_page("http://www.hltv.org/matches/")
    matchlist = matches.find_all("div", {"class": ["matchListBox", "matchListDateBox"]})
    for match in matchlist:
        if match['class'][0] == "matchListDateBox":
            print("* " + match.text)
        else:
            try:
                time = match.find("div", {"class": "matchTimeCell"}).text.strip()
                team1 = match.find("div", {"class": "matchTeam1Cell"}).text.strip()
                team2 = match.find("div", {"class": "matchTeam2Cell"}).text.strip()
                print(time + " " + team1 + " vs " + team2)
            except:
                print(match.text[:7].strip(), match.text[7:-7].strip())


if __name__ == "__main__":
    getmatches()
