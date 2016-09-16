import requests
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
            player['name'] = player_anchor.text.strip()
            player_link = player_anchor.get('href')
            if 'pageid' in player_link:
                player['player-id'] = converters.to_int(player_link[player_link.index('playerid'):], regexp=True)
            else:
                player['player-id'] = converters.to_int(player_link, regexp=True)
            if player['name'].startswith("[email"):
                player_page = get_parsed_page(str("http://www.hltv.org" + player_anchor['href']))
                player['name'] = player_page.title.text.split()[0]
            newteam['team-players'].append(player)
        teamlist.append(newteam)
    return teamlist


def top_players():
    page = get_parsed_page("http://www.hltv.org/?pageid=348&statsfilter=10&mapid=0")
    boxes = page.find_all("div", {"class": "framedBox"})
    top_player_categories = []
    for box in boxes:
        category_obj = {'category': box.find("h2").text}
        players = []
        for player_elem in box.select("> div"):
            player = {}
            player_link = player_elem.find('a')
            player['name'] = player_link.text
            player['team'] = player_elem.text.split("(")[1].split(")")[0]
            p_url = player_link['href']
            player['player-id'] = converters.to_int(p_url[p_url.index('playerid=')+9:p_url.index('&statsfilter')])
            player['stat'] = player_elem.select('div:nth-of-type(2)')[0].text
            players.append(player)
        category_obj['players'] = players
        top_player_categories.append(category_obj)
    return top_player_categories


def get_players(teamid):
    page = get_parsed_page("http://www.hltv.org/?pageid=362&teamid=" + teamid)
    titlebox = page.find("div", {"class": "centerFade"})
    players = []
    for player in titlebox.find_all("div")[5:25]:
        players.append(player.text.strip())
    print([x for x in set(players) if x is not u''])


def get_team_info(teamid):
    """
    :param teamid: integer (or string consisting of integers)
    :return: dictionary of team

    example team id: 5378 (virtus pro)
    """
    page = get_parsed_page("http://www.hltv.org/?pageid=179&teamid=" + str(teamid))

    team_info = {}

    content_boxes = page.select('div.centerFade .covGroupBoxContent')
    team_info['team-name']=content_boxes[0].select('> div')[0].text.strip()
    team_info['region'] = content_boxes[0].select('> div')[4].select('.covSmallHeadline')[1].text.strip()

    current_lineup_div = content_boxes[1]
    current_lineup = _get_lineup(current_lineup_div.select('a'))
    team_info['current-lineup'] = current_lineup

    historical_players_div = content_boxes[2]
    historical_players = _get_lineup(historical_players_div.select('a'))
    team_info['historical-players'] = historical_players

    team_stats_div = content_boxes[3]
    team_stats = {}
    for index, stat_div in enumerate(team_stats_div.select('> div')[3:]):
        if (index%2):
            stat_title = stat_div.select('.covSmallHeadline')[0].text.strip()
            stat_value = stat_div.select('.covSmallHeadline')[1].text.strip()
            team_stats[stat_title] = stat_value
    team_info['stats'] = team_stats

    return team_info


def _get_lineup(player_anchors):
    """
    helper function for function above
    :return: list of players
    """
    players = []
    for player_anchor in player_anchors:
        player = {}
        player_link = player_anchor.get('href')
        player['player-id'] = converters.to_int(player_link[player_link.index('playerid'):], regexp=True)
        player_text = player_anchor.text
        player['name'] = player_text[0:player_text.index("(")].strip()
        player['maps-played'] = converters.to_int(player_text[player_text.index("("):], regexp=True)
        players.append(player)
    return players


def get_matches():
    matches = get_parsed_page("http://www.hltv.org/matches/")
    matchlist = matches.find_all("div", {"class": ["matchListBox", "matchListDateBox"]})
    datestring = ""
    matches_list = []
    for match in matchlist:
        if match['class'][0] == "matchListDateBox":
            # TODO possibly change this into real date object
            datestring = match.text.strip()
        else:
            try:
                #What does matchd mean?
                matchd = {}
                matchd['date'] = datestring + " - " + match.find("div", {"class": "matchTimeCell"}).text.strip()
                team1div = match.find("div", {"class": "matchTeam1Cell"})
                team1 = {}
                team1["name"] = team1div.text.strip()
                team1href = team1div.select('a')[0].get('href')
                team1["id"] = converters.to_int(team1href[team1href.index('teamid'):], regexp=True)
                matchd['team1'] = team1
                team2div = match.find("div", {"class": "matchTeam2Cell"})
                team2 = {}
                team2["name"] = team2div.text.strip()
                team2href = team2div.select('a')[0].get('href')
                team2["id"] = converters.to_int(team2href[team2href.index('teamid'):], regexp=True)
                matchd['team2'] = team2
                # TODO include link (id) to match page
                matches_list.append(matchd)
            except:
                # what does this do man?
                print(match.text[:7].strip(), match.text[7:-7].strip())
    return matches_list

def get_results():
    results = get_parsed_page("http://www.hltv.org/results/")
    resultslist = results.find_all("div", {"class": ["matchListBox", "matchListDateBox"]})
    datestring = ""
    results_list = []
    for result in resultslist:
        if result['class'][0] == "matchListDateBox":
            # TODO possibly change this into a real date object
            datestring = result.text.strip()
        else:
            #What does resultd mean?
            resultd = {}
            #This page uses the time box to show map played
            resultd['date'] = datestring
            resultd['map'] = result.find("div", {"class": "matchTimeCell"}).text.strip()
            scores = result.find("div", {"class": "matchScoreCell"}).text.strip()
            
            #Team 1 info
            team1div = result.find("div", {"class": "matchTeam1Cell"})
            team1 = {}
            team1['name'] = team1div.text.strip()
            #I seem to get the ID slightly differently, still works fine though
            team1href = team1div.select('a')[0].get('href')
            team1['id'] = team1href.split("=")[-1]
            team1['score'] = scores.split("-")[0].strip()
            resultd['team1'] = team1

            #Team 2 info
            team2div = result.find("div", {"class": "matchTeam2Cell"})
            team2 = {}
            team2['name'] = team2div.text.strip()
            team2href = team2div.select('a')[0].get('href')
            team2['id'] = team2href.split("=")[-1]
            team2['score'] = scores.split("-")[1].strip()
            resultd['team2'] = team2

            results_list.append(resultd)
    return(results_list)
            
            
if __name__ == "__main__":
    print(get_results())
