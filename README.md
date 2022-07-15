# hltv-api
Provides an API for HLTV


## `top5teams`  

```python
>>> import main as hltv
>>> hltv.top5teams()
[{'id': 4608,
  'name': 'Natus Vincere',
  'url': 'https://hltv.org/team/4608/natus-vincere'},
 {'id': 6667, 'name': 'FaZe', 'url': 'https://hltv.org/team/6667/faze'},
 {'id': 4869, 'name': 'ENCE', 'url': 'https://hltv.org/team/4869/ence'},
 {'id': 5752, 'name': 'Cloud9', 'url': 'https://hltv.org/team/5752/cloud9'},
 {'id': 9565, 'name': 'Vitality', 'url': 'https://hltv.org/team/9565/vitality'}]
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
 {'id': 7412,
  'name': "Lukas 'gla1ve' Rossander",
  'nickname': 'gla1ve',
  'url': 'https://hltv.org/player/7412/gla1ve'},
 {'id': 9078,
  'name': "Kristian 'k0nfig' Wienecke",
  'nickname': 'k0nfig',
  'url': 'https://hltv.org/player/9078/k0nfig'},
 {'id': 13300,
  'name': "Asger 'Farlig' Jensen",
  'nickname': 'Farlig',
  'url': 'https://hltv.org/player/13300/farlig'},
 {'id': 15165,
  'name': "Benjamin 'blameF' Bremer",
  'nickname': 'blameF',
  'url': 'https://hltv.org/player/15165/blamef'}]
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
                    {'country': 'Denmark',
                     'id': 7412,
                     'maps-played': 1094,
                     'name': 'Lukas Rossander',
                     'nickname': 'gla1ve',
                     'url': 'https://hltv.org/stats/players/7412/gla1ve'},
                    {'country': 'Denmark',
                     'id': 9078,
                     'maps-played': 139,
                     'name': 'Kristian Wienecke',
                     'nickname': 'k0nfig',
                     'url': 'https://hltv.org/stats/players/9078/k0nfig'},
                    {'country': 'Denmark',
                     'id': 13300,
                     'maps-played': 82,
                     'name': 'Asger Jensen',
                     'nickname': 'Farlig',
                     'url': 'https://hltv.org/stats/players/13300/farlig'},
                    {'country': 'Denmark',
                     'id': 15165,
                     'maps-played': 139,
                     'name': 'Benjamin Bremer',
                     'nickname': 'blameF',
                     'url': 'https://hltv.org/stats/players/15165/blamef'}],
 'historical-players': [{'country': 'Denmark',
                         'id': 9612,
                         'maps-played': 86,
                         'name': 'Lucas Andersen',
                         'nickname': 'Bubzkji',
                         'url': 'https://hltv.org/stats/players/9612/bubzkji'},
                        {'country': 'Denmark',
                         'id': 9612,
                         'maps-played': 86,
                         'name': 'Lucas Andersen',
                         'nickname': 'Bubzkji',
                         'url': 'https://hltv.org/stats/players/9612/bubzkji'},
                        {'country': 'Denmark',
                         'id': 7592,
                         'maps-played': 1076,
                         'name': 'Nicolai Reedtz',
                         'nickname': 'device',
                         'url': 'https://hltv.org/stats/players/7592/device'},
                        {'country': 'Denmark',
                         'id': 7398,
                         'maps-played': 1179,
                         'name': 'Peter Rasmussen',
                         'nickname': 'dupreeh',
                         'url': 'https://hltv.org/stats/players/7398/dupreeh'},
                        {'country': 'Denmark',
                         'id': 8611,
                         'maps-played': 53,
                         'name': 'Patrick Hansen',
                         'nickname': 'es3tag',
                         'url': 'https://hltv.org/stats/players/8611/es3tag'},
                        {'country': 'Denmark',
                         'id': 429,
                         'maps-played': 185,
                         'name': 'Finn Andersen',
                         'nickname': 'karrigan',
                         'url': 'https://hltv.org/stats/players/429/karrigan'},
                        {'country': 'Denmark',
                         'id': 8394,
                         'maps-played': 355,
                         'name': 'Markus Kjærbye',
                         'nickname': 'Kjaerbye',
                         'url': 'https://hltv.org/stats/players/8394/kjaerbye'},
                        {'country': 'Denmark',
                         'id': 9032,
                         'maps-played': 732,
                         'name': 'Emil Reif',
                         'nickname': 'Magisk',
                         'url': 'https://hltv.org/stats/players/9032/magisk'},
                        {'country': 'Denmark',
                         'id': 21,
                         'maps-played': 12,
                         'name': 'Danny Sørensen',
                         'nickname': 'zonic',
                         'url': 'https://hltv.org/stats/players/21/zonic'},
                        {'country': 'Denmark',
                         'id': 2469,
                         'maps-played': 90,
                         'name': 'René Borg',
                         'nickname': 'cajunb',
                         'url': 'https://hltv.org/stats/players/2469/cajunb'},
                        {'country': 'Denmark',
                         'id': 13843,
                         'maps-played': 103,
                         'name': 'Philip Ewald',
                         'nickname': 'Lucky',
                         'url': 'https://hltv.org/stats/players/13843/lucky'},
                        {'country': 'Norway',
                         'id': 1485,
                         'maps-played': 10,
                         'name': 'Ruben Villarroel',
                         'nickname': 'RUBINO',
                         'url': 'https://hltv.org/stats/players/1485/rubino'},
                        {'country': 'Denmark',
                         'id': 16718,
                         'maps-played': 1,
                         'name': 'Frederik Sørensen',
                         'nickname': 'Fessor',
                         'url': 'https://hltv.org/stats/players/16718/fessor'},
                        {'country': 'Denmark',
                         'id': 9903,
                         'maps-played': 4,
                         'name': 'Anton Pedersen',
                         'nickname': 'notaN',
                         'url': 'https://hltv.org/stats/players/9903/notan'},
                        {'country': 'Denmark',
                         'id': 8783,
                         'maps-played': 15,
                         'name': 'Jakob Hansen',
                         'nickname': 'JUGi',
                         'url': 'https://hltv.org/stats/players/8783/jugi'},
                        {'country': 'Denmark',
                         'id': 7154,
                         'maps-played': 4,
                         'name': 'Jacob Winneche',
                         'nickname': 'Pimp',
                         'url': 'https://hltv.org/stats/players/7154/pimp'},
                        {'country': 'Denmark',
                         'id': 922,
                         'maps-played': 9,
                         'name': 'Marco Pfeiffer',
                         'nickname': 'Snappi',
                         'url': 'https://hltv.org/stats/players/922/snappi'},
                        {'country': 'Sweden',
                         'id': 1146,
                         'maps-played': 8,
                         'name': 'Dennis Edman',
                         'nickname': 'dennis',
                         'url': 'https://hltv.org/stats/players/1146/dennis'}],
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
