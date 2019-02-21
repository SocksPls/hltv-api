import re
import requests
import datetime
from bs4 import BeautifulSoup
from python_utils import converters


def get_parsed_page(url):
    # This fixes a blocked by cloudflare error i've encountered
    headers = {
        "referer": "https://www.hltv.org/stats",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")


def top5teams():
    home = get_parsed_page("http://hltv.org/")
    count = 0
    teams = []
    for team in home.find_all("div", {"class": ["col-box rank"], }):
        count += 1
        teamname = team.text[3:]
        teams.append(teamname)
    return teams


def top30teams():
    page = get_parsed_page("http://www.hltv.org/ranking/teams/")
    teams = page.find("div", {"class": "ranking"})
    teamlist = []
    for team in teams.find_all("div", {"class": "ranked-team standard-box"}):
        newteam = {'name': team.find('div', {"class": "ranking-header"}).select('.name')[0].text.strip(),
                   'rank': converters.to_int(team.select('.position')[0].text.strip(), regexp=True),
                   'rank-points': converters.to_int(team.find('span', {'class': 'points'}).text, regexp=True),
                   'team-id': converters.to_int(team.find('a', {'class': 'details moreLink'})['href'].split('/')[-1]),
                   'team-players': []}
        for player_div in team.find_all("td", {"class": "player-holder"}):
            player = {}
            player['name'] = player_div.find('img', {'class': 'playerPicture'})['title']
            player['player-id'] = converters.to_int(player_div.select('.pointer')[0]['href'].split("/")[-2])
            newteam['team-players'].append(player)
        teamlist.append(newteam)
    return teamlist


def top_players():
    page = get_parsed_page("https://www.hltv.org/stats")
    players = page.find_all("div", {"class": "col"})[0]
    playersArray = []
    for player in players.find_all("div", {"class": "top-x-box standard-box"}):
        playerObj = {}
        playerObj['country'] = player.find_all('img')[1]['alt'].encode('utf8')
        buildName = player.find('img', {'class': 'img'})['alt'].split("'")
        playerObj['name'] = buildName[0].rstrip() + buildName[2]
        playerObj['nickname'] = player.find('a', {'class': 'name'}).text.encode('utf8')
        playerObj['rating'] = player.find('div', {'class': 'rating'}).find('span', {'class': 'bold'}).text.encode('utf8')
        playerObj['maps-played'] = player.find('div', {'class': 'average gtSmartphone-only'}).find('span', {'class': 'bold'}).text.encode('utf8')

        playersArray.append(playerObj)
    return playersArray


def get_players(teamid):
    page = get_parsed_page("http://www.hltv.org/?pageid=362&teamid=" + str(teamid))
    titlebox = page.find("div", {"class": "bodyshot-team"})
    players = []
    for player_link in titlebox.find_all("a"):
        players.append(player_link['title'])

    return players


def get_team_info(teamid):
    """
    :param teamid: integer (or string consisting of integers)
    :return: dictionary of team

    example team id: 5378 (virtus pro)
    """
    page = get_parsed_page("http://www.hltv.org/?pageid=179&teamid=" + str(teamid))

    team_info = {}
    team_info['team-name']=page.find("div", {"class": "context-item"}).text.encode('utf8')

    current_lineup = _get_current_lineup(page.find_all("div", {"class": "col teammate"}))
    team_info['current-lineup'] = current_lineup

    historical_players = _get_historical_lineup(page.find_all("div", {"class": "col teammate"}))
    team_info['historical-players'] = historical_players

    team_stats_columns = page.find_all("div", {"class": "columns"})
    team_stats = {}

    for columns in team_stats_columns:
        stats = columns.find_all("div", {"class": "col standard-box big-padding"})

        for stat in stats:
            stat_value = stat.find("div", {"class": "large-strong"}).text.encode('utf8')
            stat_title = stat.find("div", {"class": "small-label-below"}).text.encode('utf8')
            team_stats[stat_title] = stat_value

    team_info['stats'] = team_stats

    return team_info


def _get_current_lineup(player_anchors):
    """
    helper function for function above
    :return: list of players
    """
    players = []
    for player_anchor in player_anchors[0:5]:
        player = {}
        buildName = player_anchor.find("img", {"class": "container-width"})["alt"].split('\'')
        player['country'] = player_anchor.find("div", {"class": "teammate-info standard-box"}).find("img", {"class": "flag"})["alt"]
        player['name'] = buildName[0].rstrip() + buildName[2]
        player['nickname'] = player_anchor.find("div", {"class": "teammate-info standard-box"}).find("div", {"class": "text-ellipsis"}).text
        player['maps-played'] = int(re.search(r'\d+', player_anchor.find("div", {"class": "teammate-info standard-box"}).find("span").text).group())
        players.append(player)
    return players

def _get_historical_lineup(player_anchors):
    """
    helper function for function above
    :return: list of players
    """
    players = []
    for player_anchor in player_anchors[5::]:
        player = {}
        buildName = player_anchor.find("img", {"class": "container-width"})["alt"].split('\'')
        player['country'] = player_anchor.find("div", {"class": "teammate-info standard-box"}).find("img", {"class": "flag"})["alt"].encode('utf8')
        player['name'] = buildName[0].rstrip() + buildName[2]
        player['nickname'] = player_anchor.find("div", {"class": "teammate-info standard-box"}).find("div", {"class": "text-ellipsis"}).text.encode('utf8')
        player['maps-played'] = int(re.search(r'\d+', player_anchor.find("div", {"class": "teammate-info standard-box"}).find("span").text).group())
        players.append(player)
    return players


def get_matches():
    matches = get_parsed_page("http://www.hltv.org/matches/")
    matches_list = []
    upcomingmatches = matches.find("div", {"class": "upcoming-matches"})

    matchdays = upcomingmatches.find_all("div", {"class": "match-day"})

    for match in matchdays:
        matchDetails = match.find_all("table", {"class": "table"})

        for getMatch in matchDetails:
            matchObj = {}

            matchObj['date'] = match.find("span", {"class": "standard-headline"}).text.encode('utf8')
            matchObj['time'] = getMatch.find("td", {"class": "time"}).text.encode('utf8').lstrip().rstrip()

            if (getMatch.find("td", {"class": "placeholder-text-cell"})):
                matchObj['event'] = getMatch.find("td", {"class": "placeholder-text-cell"}).text.encode('utf8')
            elif (getMatch.find("td", {"class": "event"})):
                matchObj['event'] = getMatch.find("td", {"class": "event"}).text.encode('utf8')
            else:
                matchObj['event'] = None

            if (getMatch.find_all("td", {"class": "team-cell"})):
                matchObj['team1'] = getMatch.find_all("td", {"class": "team-cell"})[0].text.encode('utf8').lstrip().rstrip()
                matchObj['team2'] = getMatch.find_all("td", {"class": "team-cell"})[1].text.encode('utf8').lstrip().rstrip()
            else:
                matchObj['team1'] = None
                matchObj['team2'] = None

            matches_list.append(matchObj)

    return matches_list

def get_results():
    results = get_parsed_page("http://www.hltv.org/results/")

    results_list = []

    pastresults = results.find_all("div", {"class": "results-holder"})

    for result in pastresults:
        resultDiv = result.find_all("div", {"class": "result-con"})

        for res in resultDiv:
            getRes = res.find("div", {"class": "result"}).find("table")

            resultObj = {}

            if (res.parent.find("span", {"class": "standard-headline"})):
                resultObj['date'] = res.parent.find("span", {"class": "standard-headline"}).text.encode('utf8')
            else:
                dt = datetime.date.today()
                resultObj['date'] = str(dt.day) + '/' + str(dt.month) + '/' + str(dt.year)

            if (res.find("td", {"class": "placeholder-text-cell"})):
                resultObj['event'] = res.find("td", {"class": "placeholder-text-cell"}).text.encode('utf8')
            elif (res.find("td", {"class": "event"})):
                resultObj['event'] = res.find("td", {"class": "event"}).text.encode('utf8')
            else:
                resultObj['event'] = None

            if (res.find_all("td", {"class": "team-cell"})):
                resultObj['team1'] = res.find_all("td", {"class": "team-cell"})[0].text.encode('utf8').lstrip().rstrip()
                resultObj['team1score'] = converters.to_int(res.find("td", {"class": "result-score"}).find_all("span")[0].text.encode('utf8').lstrip().rstrip())
                resultObj['team2'] = res.find_all("td", {"class": "team-cell"})[1].text.encode('utf8').lstrip().rstrip()
                resultObj['team2score'] = converters.to_int(res.find("td", {"class": "result-score"}).find_all("span")[1].text.encode('utf8').lstrip().rstrip())
            else:
                resultObj['team1'] = None
                resultObj['team2'] = None

            results_list.append(resultObj)

    return results_list

def get_results_by_date(start_date, end_date):
    # Dates like yyyy-mm-dd  (iso)
    results_list = []
    offset = 0
    # Loop through all stats pages
    while True:
        url = "https://www.hltv.org/stats/matches?startDate="+start_date+"&endDate="+end_date+"&offset="+str(offset)

        results = get_parsed_page(url)

        # Total amount of results of the query
        amount = int(results.find("span", attrs={"class": "pagination-data"}).text.split("of")[1].strip())

        # All rows (<tr>s) of the match table
        pastresults = results.find("tbody").find_all("tr")

        # Parse each <tr> element to a result dictionary
        for result in pastresults:
            team_cols = result.find_all("td", {"class": "team-col"})
            t1 = team_cols[0].find("a").text
            t2 = team_cols[1].find("a").text
            t1_score = int(team_cols[0].find_all(attrs={"class": "score"})[0].text.strip()[1:-1])
            t2_score = int(team_cols[1].find_all(attrs={"class": "score"})[0].text.strip()[1:-1])
            map = result.find(attrs={"class": "statsDetail"}).find(attrs={"class": "dynamic-map-name-full"}).text
            event = result.find(attrs={"class": "event-col"}).text
            date = result.find(attrs={"class": "date-col"}).find("a").find("div").text

            result_dict = {"team1": t1, "team2": t2, "team1score": t1_score,
                           "team2score": t2_score, "date": date, "map": map, "event": event}

            # Add this pages results to the result list
            results_list.append(result_dict)

        # Get the next 50 results (next page) or break
        if offset < amount:
            offset += 50
        else:
            break

    return results_list

if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter()
    
    pp.pprint('top5')
    pp.pprint(top5teams())

    pp.pprint('top30')
    pp.pprint(top30teams())
    
    pp.pprint('top_players')
    pp.pprint(top_players())
    
    pp.pprint('get_players')
    pp.pprint(get_players('6665'))
    
    pp.pprint('get_team_info')
    pp.pprint(get_team_info('6665'))

    pp.pprint('get_matches')
    pp.pprint(get_matches())

    pp.pprint('get_results')
    pp.pprint(get_results())

    pp.pprint('get_results_by_date')
    today_iso = datetime.datetime.today().isoformat().split('T')[0]
    pp.pprint(get_results_by_date(today_iso, today_iso))
   