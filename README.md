# hltv-api
Provides an API for HLTV


## `top5teams`  

```python
>>> import main as hltv
>>> hltv.top5teams()
['Vitality', 'Heroic', 'Astralis', 'Natus Vincere', 'BIG']
```

## `top30teams`  

```python
>>> hltv.top30teams()
[{'name': 'Vitality',
  'rank': 1,
  'rank-points': 913,
  'team-id': 9565,
  'team-players': [{'name': "Richard 'shox' Papillon", 'player-id': 1225},
   {'name': "Cédric 'RpK' Guipouy", 'player-id': 7169},
   {'name': "Dan 'apEX' Madesclaire", 'player-id': 7322},
   {'name': "Mathieu 'ZywOo' Herbaut", 'player-id': 11893},
   {'name': "Kévin 'misutaaa' Rabier", 'player-id': 14176}]},
  ...
}]
```

## `top_players`  

```python
>>> hltv.top_players()
[{'country': b'France',
  'name': 'Mathieu Herbaut',
  'nickname': b'ZywOo',
  'rating': b'1.28',
  'maps-played': b'733'},
  ...
}]
```

## `get_players`  

```python
>>> hltv.get_players("6665")
[{'id': '4954', 'nickname': 'Xyp9x', 'name': "Andreas 'Xyp9x' Højsleth"},
 {'id': '7398', 'nickname': 'dupreeh', 'name': "Peter 'dupreeh' Rasmussen"},
 {'id': '7412', 'nickname': 'gla1ve', 'name': "Lukas 'gla1ve' Rossander"},
 {'id': '7592', 'nickname': 'device', 'name': "Nicolai 'device' Reedtz"},
 {'id': '9032', 'nickname': 'Magisk', 'name': "Emil 'Magisk' Reif"}]
```

## `get_player_info`

```python
>>>hltv.get_player_info('7398')
{'nickname': b'dupreeh',
 'name': b'Peter Rasmussen',
 'country': 'Denmark',
 'team': b'Astralis',
 'age': '27',
 'stats': {'total_kills': '32442',
  'headshot_percent': '50.6%',
  'total_deaths': '28386',
  'kd_ratio': '1.14',
  'dmg_per_round': '78.2',
  'grenade_dmg_per_round': '3.0',
  'maps_played': '1690',
  'rounds_played': '43830',
  'kills_per_round': '0.74',
  'assists_per_round': '0.14',
  'deaths_per_round': '0.65',
  'saved_by_teammate_per_round': '0.10',
  'saved_teammates_per_round': '0.09',
  'rating_1': '1.09'}}
```

## `get_team_info`  

```python
>>> hltv.get_team_info("6667")
{'team-name': b'FaZe',
 'current-lineup': [{'country': 'Sweden',
   'name': 'Olof Kajbjer',
   'nickname': 'olofmeister',
   'maps-played': 543},
  {'country': 'Norway',
   'name': 'Håvard Nygaard',
   'nickname': 'rain',
   'maps-played': 1044},
  {'country': 'Denmark',
   'name': 'Markus Kjærbye',
   'nickname': 'Kjaerbye',
   'maps-played': 59},
  {'country': 'Brazil',
   'name': 'Marcelo David',
   'nickname': 'coldzera',
   'maps-played': 233},
  {'country': 'Latvia',
   'name': 'Helvijs Saukants',
   'nickname': 'broky',
   'maps-played': 233}],
 'historical-players': [{'country': b'Poland',
   'name': 'Filip Kubski',
   'nickname': b'NEO',
   'maps-played': 45},
  {'country': b'Slovakia',
   'name': 'Ladislav Kovács',
   'nickname': b'GuardiaN',
   'maps-played': 484},
  {'country': b'Lithuania',
   'name': 'Aurimas Pipiras',
   'nickname': b'Bymas',
   'maps-played': 41},
  {'country': b'Denmark',
   'name': 'Finn Andersen',
   'nickname': b'karrigan',
   'maps-played': 548},
  {'country': b'Kazakhstan',
   'name': 'Dauren Kystaubayev',
   'nickname': b'AdreN',
   'maps-played': 65},
  {'country': b'Sweden',
   'name': 'Richard Landström',
   'nickname': b'Xizt',
   'maps-played': 59},
  {'country': b'Sweden',
   'name': 'Mikail Bill',
   'nickname': b'Maikelele',
   'maps-played': 25},
  {'country': b'Portugal',
   'name': 'Ricardo Pacheco',
   'nickname': b'fox',
   'maps-played': 88},
  {'country': b'Finland',
   'name': 'Aleksi Jalli',
   'nickname': b'allu',
   'maps-played': 237},
  {'country': b'Norway',
   'name': 'Joakim Myrbostad',
   'nickname': b'jkaem',
   'maps-played': 180},
  {'country': b'Norway',
   'name': 'Jorgen Robertsen',
   'nickname': b'cromen',
   'maps-played': 27},
  {'country': b'Bosnia and Herzegovina',
   'name': 'Nikola Kovač',
   'nickname': b'NiKo',
   'maps-played': 799},
  {'country': b'Denmark',
   'name': 'Philip Aistrup',
   'nickname': b'aizy',
   'maps-played': 218},
  {'country': b'France',
   'name': 'Fabien Fiey',
   'nickname': b'kioShiMa',
   'maps-played': 280},
  {'country': b'Sweden',
   'name': 'Robert Dahlström',
   'nickname': b'RobbaN',
   'maps-played': 2},
  {'country': b'Australia',
   'name': 'Karlo Pivac',
   'nickname': b'USTILO',
   'maps-played': 1},
  {'country': b'Denmark',
   'name': 'Jesper Plougmann',
   'nickname': b'TENZKI',
   'maps-played': 2},
  {'country': b'Serbia',
   'name': 'Janko Paunović',
   'nickname': b'YNk',
   'maps-played': 8},
  {'country': b'Sweden',
   'name': 'Zebastian Molinder',
   'nickname': b'zbM',
   'maps-played': 1}],
 'stats': {b'Maps played': b'1044',
  b'Wins / draws / losses': b'593 / 5 / 446',
  b'Total kills': b'94441',
  b'Total deaths': b'89842',
  b'Rounds played': b'27494',
  b'K/D Ratio': b'1.05'}}
```

## `get_match_info`
```python
>>> get_match_info("77841")
{'team1': {'name': 'Astralis',
  'players': ['device', 'Magisk', 'Xyp9x', 'dupreeh', 'gla1ve'],
  'device': {'kills': '67',
   'headshots': '23',
   'assists': '17',
   'flash_assists': '7',
   'deaths': '61',
   'kast': '71.9%',
   'kd_diff': '+6',
   'adr': '84.8',
   'fk_diff': '+7',
   'rating': '1.17'},
  'Magisk': {'kills': '59',
   'headshots': '25',
   'assists': '12',
   'flash_assists': '3',
   'deaths': '64',
   'kast': '68.5%',
   'kd_diff': '-5',
   'adr': '77.3',
   'fk_diff': '+4',
   'rating': '1.03'},
  'Xyp9x': {'kills': '58',
   'headshots': '24',
   'assists': '22',
   'flash_assists': '8',
   'deaths': '58',
   'kast': '69.7%',
   'kd_diff': '0',
   'adr': '72.6',
   'fk_diff': '+1',
   'rating': '1.02'},
  'dupreeh': {'kills': '56',
   'headshots': '33',
   'assists': '15',
   'flash_assists': '2',
   'deaths': '61',
   'kast': '66.3%',
   'kd_diff': '-5',
   'adr': '59.7',
   'fk_diff': '+1',
   'rating': '0.94'},
  'gla1ve': {'kills': '45',
   'headshots': '19',
   'assists': '22',
   'flash_assists': '9',
   'deaths': '65',
   'kast': '60.7%',
   'kd_diff': '-20',
   'adr': '62.5',
   'fk_diff': '-8',
   'rating': '0.79'}},
 'team2': {'name': 'G2',
  'players': ['NiKo', 'huNter-', 'AmaNEk', 'nexa', 'kennyS'],
  'NiKo': {'kills': '67',
   'headshots': '23',
   'assists': '17',
   'flash_assists': '7',
   'deaths': '61',
   'kast': '71.9%',
   'kd_diff': '+6',
   'adr': '84.8',
   'fk_diff': '+7',
   'rating': '1.17'},
  'huNter-': {'kills': '59',
   'headshots': '25',
   'assists': '12',
   'flash_assists': '3',
   'deaths': '64',
   'kast': '68.5%',
   'kd_diff': '-5',
   'adr': '77.3',
   'fk_diff': '+4',
   'rating': '1.03'},
  'AmaNEk': {'kills': '58',
   'headshots': '24',
   'assists': '22',
   'flash_assists': '8',
   'deaths': '58',
   'kast': '69.7%',
   'kd_diff': '0',
   'adr': '72.6',
   'fk_diff': '+1',
   'rating': '1.02'},
  'nexa': {'kills': '56',
   'headshots': '33',
   'assists': '15',
   'flash_assists': '2',
   'deaths': '61',
   'kast': '66.3%',
   'kd_diff': '-5',
   'adr': '59.7',
   'fk_diff': '+1',
   'rating': '0.94'},
  'kennyS': {'kills': '45',
   'headshots': '19',
   'assists': '22',
   'flash_assists': '9',
   'deaths': '65',
   'kast': '60.7%',
   'kd_diff': '-20',
   'adr': '62.5',
   'fk_diff': '-8',
   'rating': '0.79'}}}
```


## `get_matches`  

```python
>>> hltv.get_matches()
[{'date': '2022-06-06',
  'event': b'WePlay Academy League Season 4',
  'team1': b'Astralis Talent',
  'team2': b'Apeks Rebels',
  'time': '18:10',
  'url': 'https://hltv.org/matches/2356247/esl-impact-league-season-1-finals-grand-final-esl-impact-league-season-1-finals'},
  ...
]
```

## `get_results`

```python
>>> hltv.get_results()
[{'date': '10/11/2020',
  'event': b'IEM Beijing-Haidian 2020 North America',
  'team1': b'Liquid',
  'team1score': 2,
  'team2': b'Chaos',
  'team2score': 0},
  ...
}]
```

## `get_results_by_date`

```python
>>> hltv.get_results_by_date()
[{'team2score': 16, 'team1': 'AGO', 'team2': 'G2', 'team1score': 8, 'map': 'Inferno', 'date': '2018-2-15', 'event': 'ESL Pro League Season 7 Europe'}, ... ]
```
