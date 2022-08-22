# hltv-api
Provides an API for HLTV


## `top5teams`  

```python
>>> import main as hltv
>>> hltv.top5teams()
[{'id': 4608,
  'name': 'Natus Vincere',
  'url': 'https://hltv.org/team/4608/natus-vincere'},
  ...]
```

## `top30teams`  

```python
>>> hltv.top30teams()
[{'name': 'Natus Vincere',
  'rank': 1,
  'rank-points': 935,
  'stats-url': 'https://www.hltv.org/ranking/teams/2022/july/11/details/4608',
  'team-id': 4608,
  'team-players': [{'name': "Aleksandr 's1mple' Kostyliev",
                    'player-id': 7998,
                    'url': 'https://www.hltv.org/player/7998/s1mple'},
                    ...],
  'team-url': 'https://hltv.org/team/4608/Natus Vincere'},
  ...
]
```

## `top_players`  

```python
>>> hltv.top_players()
[{'country': 'France',
  'id': 11893,
  'maps-played': '1020',
  'name': 'Mathieu Herbaut',
  'nickname': 'ZywOo',
  'rating': '1.27',
  'url': 'https://hltv.org/stats/players/11893/zywoo'},
  ...
}]
```

## `get_players`  

```python
>>> hltv.get_players("6665")
[{'id': 4954,
  'name': "Andreas 'Xyp9x' Højsleth",
  'nickname': 'Xyp9x',
  'url': 'https://hltv.org/player/4954/xyp9x'},
  ...]
```

## `get_team_info`  

```python
>>> hltv.get_team_info("6665")
{'current-lineup': [{'country': 'Denmark',
                     'id': 4954,
                     'maps-played': 1239,
                     'name': 'Andreas Højsleth',
                     'nickname': 'Xyp9x',
                     'url': 'https://hltv.org/stats/players/4954/xyp9x'},
                     ...],
 'historical-players': [{'country': 'Denmark',
                         'id': 9612,
                         'maps-played': 86,
                         'name': 'Lucas Andersen',
                         'nickname': 'Bubzkji',
                         'url': 'https://hltv.org/stats/players/9612/bubzkji'},
                         ...],
 'matches': [{'championship': 'BLAST Premier Fall Groups 2022',
              'confront_name': 'Astralis X Ninjas in Pyjamas',
              'date': '2022-08-19',
              'teams': {'team_1': 'Astralis',
                        'team_1_id': 6665,
                        'team_2': 'Ninjas in Pyjamas',
                        'team_2_id': 4411},
              'time': '14:00',
              'match_id': 2357643,
              'url': 'https://hltv.org/matches/2357643/astralis-vs-ninjas-in-pyjamas-blast-premier-fall-groups-2022'},
              ...]
 'stats': {'K/D Ratio': '1.10',
           'Maps played': '1323',
           'Rounds played': '34752',
           'Total deaths': '110203',
           'Total kills': '120679',
           'Wins / draws / losses': '860 / 2 / 461'},
 'team-id': 6665,
 'team-name': 'Astralis',
 'url': 'https://hltv.org/stats/team/6665/Astralis'}
```

## `get_matches`  

```python
>>> hltv.get_matches()
[{'countdown': '0:13:00',
  'date': '2022-07-14',
  'event': 'ESL Challenger Melbourne 2022 Europe Closed Qualifier',
  'match-id': 2357360,
  'team1': 'HEET',
  'team1-id': 11501,
  'team2': 'Entropiq',
  'team2-id': 10831,
  'time': '15:30',
  'url': 'https://hltv.org/matches/2357360/heet-vs-entropiq-esl-challenger-melbourne-2022-europe-closed-qualifier'},
  ...
]
```

## `get_results`

```python
>>> hltv.get_results()
[{'date': '2022-07-14',
  'event': 'ESL Challenger Melbourne 2022 Asia Closed Qualifier',
  'match-id': 2357387,
  'team1': 'YK',
  'team1-id': 11542,
  'team1score': 0,
  'team2': 'Wings Up',
  'team2-id': 10851,
  'team2score': 2,
  'url': 'https://hltv.org/matches/2357387/yk-vs-wings-up-esl-challenger-melbourne-2022-asia-closed-qualifier'},
  ...
]
```

## `get_results_by_date`

```python
>>> hltv.get_results_by_date()
[{'date': '2022-07-14',
  'event': 'ESL Challenger Melbourne 2022 Oceania Closed Qualifier',
  'map': 'Dust2',
  'match-id': 140752,
  'team1': 'VERTEX',
  'team1-id': 10672,
  'team1score': 16,
  'team2': 'Encore',
  'team2-id': 11726,
  'team2score': 6,
  'url': 'https://hltv.org/stats/matches/mapstatsid/140752/vertex-vs-encore?startDate=2022-07-14&endDate=2022-07-14'},
  ...
]
```

## `get_match_countdown`

```python
>>> hltv.get_match_countdown(2357395)
'1:29:00'
```
