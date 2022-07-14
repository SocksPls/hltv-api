# hltv-api
Provides an API for HLTV


## `top5teams`  

```python
>>> import main as hltv
>>> hltv.top5teams()
[{'name': 'Natus Vincere', 'url': 'https://hltv.org/team/4608/natus-vincere'},
 {'name': 'FaZe', 'url': 'https://hltv.org/team/6667/faze'},
 {'name': 'ENCE', 'url': 'https://hltv.org/team/4869/ence'},
 {'name': 'Cloud9', 'url': 'https://hltv.org/team/5752/cloud9'},
 {'name': 'Vitality', 'url': 'https://hltv.org/team/9565/vitality'}]
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
                   {'name': "Denis 'electroNic' Sharipov",
                    'player-id': 8918,
                    'url': 'https://www.hltv.org/player/8918/electronic'},
                   {'name': "Viktor 'sdy' Orudzhev",
                    'player-id': 12731,
                    'url': 'https://www.hltv.org/player/12731/sdy'},
                   {'name': "Ilya 'Perfecto' Zalutskiy",
                    'player-id': 16947,
                    'url': 'https://www.hltv.org/player/16947/perfecto'},
                   {'name': "Valeriy 'b1t' Vakhovskiy",
                    'player-id': 18987,
                    'url': 'https://www.hltv.org/player/18987/b1t'}],
  'team-url': 'https://hltv.org/team/4608/Natus Vincere'},
  ...
]
```

## `top_players`  

```python
>>> hltv.top_players()
[{'country': 'France',
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
[{'id': '4954',
  'name': "Andreas 'Xyp9x' Højsleth",
  'nickname': 'Xyp9x',
  'url': 'https://hltv.org/player/4954/xyp9x'},
 {'id': '7412',
  'name': "Lukas 'gla1ve' Rossander",
  'nickname': 'gla1ve',
  'url': 'https://hltv.org/player/7412/gla1ve'},
 {'id': '9078',
  'name': "Kristian 'k0nfig' Wienecke",
  'nickname': 'k0nfig',
  'url': 'https://hltv.org/player/9078/k0nfig'},
 {'id': '13300',
  'name': "Asger 'Farlig' Jensen",
  'nickname': 'Farlig',
  'url': 'https://hltv.org/player/13300/farlig'},
 {'id': '15165',
  'name': "Benjamin 'blameF' Bremer",
  'nickname': 'blameF',
  'url': 'https://hltv.org/player/15165/blamef'}]
```

## `get_team_info`  

```python
>>> hltv.get_team_info("6665")
{'current-lineup': [{'country': 'Denmark',
                     'maps-played': 1239,
                     'name': 'Andreas Højsleth',
                     'nickname': 'Xyp9x',
                     'url': 'https://hltv.org/stats/players/4954/xyp9x'},
                    {'country': 'Denmark',
                     'maps-played': 1094,
                     'name': 'Lukas Rossander',
                     'nickname': 'gla1ve',
                     'url': 'https://hltv.org/stats/players/7412/gla1ve'},
                    {'country': 'Denmark',
                     'maps-played': 139,
                     'name': 'Kristian Wienecke',
                     'nickname': 'k0nfig',
                     'url': 'https://hltv.org/stats/players/9078/k0nfig'},
                    {'country': 'Denmark',
                     'maps-played': 82,
                     'name': 'Asger Jensen',
                     'nickname': 'Farlig',
                     'url': 'https://hltv.org/stats/players/13300/farlig'},
                    {'country': 'Denmark',
                     'maps-played': 139,
                     'name': 'Benjamin Bremer',
                     'nickname': 'blameF',
                     'url': 'https://hltv.org/stats/players/15165/blamef'}],
 'historical-players': [{'country': 'Denmark',
                         'maps-played': 86,
                         'name': 'Lucas Andersen',
                         'nickname': 'Bubzkji',
                         'url': 'https://hltv.org/stats/players/9612/bubzkji'},
                        {'country': 'Denmark',
                         'maps-played': 86,
                         'name': 'Lucas Andersen',
                         'nickname': 'Bubzkji',
                         'url': 'https://hltv.org/stats/players/9612/bubzkji'},
                        {'country': 'Denmark',
                         'maps-played': 1076,
                         'name': 'Nicolai Reedtz',
                         'nickname': 'device',
                         'url': 'https://hltv.org/stats/players/7592/device'},
                         ...
                         ],
 'stats': {'K/D Ratio': '1.10',
           'Maps played': '1323',
           'Rounds played': '34752',
           'Total deaths': '110203',
           'Total kills': '120679',
           'Wins / draws / losses': '860 / 2 / 461'},
 'team-name': 'Astralis',
 'url': 'https://hltv.org/stats/team/6665/Astralis'}
```

## `get_matches`  

```python
>>> hltv.get_matches()
[{'countdown': '1:15:00',
  'date': '2022-07-14',
  'event': 'ESL Challenger Melbourne 2022 Asia Closed Qualifier',
  'team1': 'IHC',
  'team2': 'Wings Up',
  'time': '15:00',
  'url': 'https://hltv.org/matches/2357388/ihc-vs-wings-up-esl-challenger-melbourne-2022-asia-closed-qualifier'},
  ...
]
```

## `get_results`

```python
>>> hltv.get_results()
[{'date': '2022-07-14',
  'event': 'ESL Challenger Melbourne 2022 Asia Closed Qualifier',
  'team1': 'YK',
  'team1score': 0,
  'team2': 'Wings Up',
  'team2score': 2,
  'url': 'https://hltv.org/matches/2357387/yk-vs-wings-up-esl-challenger-melbourne-2022-asia-closed-qualifier'},
  ...
]
```

## `get_results_by_date`

```python
>>> hltv.get_results_by_date()
[{'date': '2022-07-14',
  'event': 'ESL Challenger Melbourne 2022 Asia Closed Qualifier',
  'map': 'Overpass',
  'team1': 'Wings Up',
  'team1score': 16,
  'team2': 'YK',
  'team2score': 8,
  'url': 'https://hltv.org/stats/matches/mapstatsid/140750/wings-up-vs-yk?startDate=2022-07-14&endDate=2022-07-14'},
  ...
]
```
