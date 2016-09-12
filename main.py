import requests
import json
from bs4 import BeautifulSoup
from python_utils import converters


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


def top20teams():
    page = get_parsed_page("http://www.hltv.org/ranking/teams/")
    teams = page.select("div.ranking-box")
    teamlist = []
    for team in teams:
        newteam = {'name': team.select('.ranking-teamName > a')[0].text.strip(),
                   'rank': converters.to_int(team.select('.ranking-number')[0].text.strip(), regexp=True),
                   'rank-points': converters.to_int(team.select('.ranking-teamName > span')[0].text, regexp=True),
                   'team-id': converters.to_int(team.select('.ranking-delta')[0].get('id'), regexp=True),
                   'team-players': []}
        for player_div in team.select('.ranking-lineup > div'):
            player = {}
            player_anchor = player_div.select('.ranking-playerNick > a')[0]
            player['player-id'] = converters.to_int(player_anchor.get('href'), regexp=True)
            if player['player-id'] == 1916:
                player['name'] = "seang@res"
            newteam['team-players'].append(player)
        teamlist.append(newteam)
    return teamlist



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
    print(top20teams())
