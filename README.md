# hltv-api
Provides an API for HLTV


## `top5teams`  

```python
>>> import main as hltv
>>> hltv.top5teams()
[u'FaZe', u'SK', u'Cloud9', u'G2', u'fnatic']
```

## `top30teams`  

```python
>>> hltv.top30teams()
[{'team-players': [{'name': "Finn 'karrigan' Andersen", 'player-id': 429}, {'name': "Olof 'olofmeister' Kajbjer", 'player-id': 885}, {'name': u"Ladislav 'GuardiaN' Kov\xe1cs", 'player-id': 2757}, {'name': u"Nikola 'NiKo' Kova\u010d", 'player-id': 3741}, {'name': u"H\xe5vard 'rain' Nygaard", 'player-id': 8183}], 'team-id': 6667, 'name': u'FaZe', 'rank': 1, 'rank-points': 919}, ... ]
```

## `top_players`  

```python
>>> hltv.top_players()
[{'maps-played': '685', 'country': 'Turkey', 'nickname': 'XANTARES', 'name': 'Ismailcan D\xc3\xb6rtkarde\xc5\x9f', 'rating': '1.25'}, ... ]
```

## `get_players`  

```python
>>> hltv.get_players("6665")
[{'id': '7398', 'nickname': 'dupreeh'}, {'id': '7412', 'nickname': 'gla1ve'}, {'id': '7592', 'nickname': 'device'}, {'id': '9032', 'nickname': 'Magisk'}, {'id': '9612', 'nickname': 'Bubzkji'}]
```

## `get_player_info`

```python
>>> hltv.get_player_info("3741")
{'id': 3741, 'nickname': b'NiKo', 'name': b'Nikola Kova\xc4\x8d', 'country': 'Bosnia and Herzegovina', 'team': b'FaZe', 'age': 23, b'Total kills': b'26979', b'Headshot %': b'50.3%', b'Total deaths': b'22562', b'K/D Ratio': b'1.20', b'Damage / Round': b'85.6', b'Grenade dmg / Round': b'3.8', b'Maps played': b'1277', b'Rounds played': b'33693', b'Kills / round': b'0.80', b'Assists / round': b'0.13', b'Deaths / round': b'0.67', b'Saved by teammate / round': b'0.08', b'Saved teammates / round': b'0.10', b'Rating 1.0': b'1.16'}
```

## `get_team_info`  

```python
>>> hltv.get_team_info("6667")
{'team-name': b'FaZe', 'current-lineup': [{'country': 'Bosnia and Herzegovina', 'name': 'Nikola Kovač', 'nickname': 'NiKo', 'maps-played': 759, 'id': 3741}, {'country': 'Norway', 'name': 'Håvard Nygaard', 'nickname': 'rain', 'maps-played': 994, 'id': 8183}, {'country': 'Denmark', 'name': 'Markus Kjærbye', 'nickname': 'Kjaerbye', 'maps-played': 9, 'id': 8394}, {'country': 'Brazil', 'name': 'Marcelo David', 'nickname': 'coldzera', 'maps-played': 183, 'id': 9216}, {'country': 'Latvia', 'name': 'Helvijs Saukants', 'nickname': 'broky', 'maps-played': 183, 'id': 18053}], 'historical-players': [{'country': b'Poland', 'name': 'Filip Kubski', 'nickname': b'NEO', 'maps-played': 45, 'id': 165}, {'country': b'Slovakia', 'name': 'Ladislav Kovács', 'nickname': b'GuardiaN', 'maps-played': 484, 'id': 2757}, {'country': b'Lithuania', 'name': 'Aurimas Pipiras', 'nickname': b'Bymas', 'maps-played': 41, 'id': 19015}, {'country': b'Denmark', 'name': 'Finn Andersen', 'nickname': b'karrigan', 'maps-played': 548, 'id': 429}, {'country': b'Kazakhstan', 'name': 'Dauren Kystaubayev', 'nickname': b'AdreN', 'maps-played': 65, 'id': 334}, {'country': b'Sweden', 'name': 'Richard Landström', 'nickname': b'Xizt', 'maps-played': 59, 'id': 884}, {'country': b'Sweden', 'name': 'Mikail Bill', 'nickname': b'Maikelele', 'maps-played': 25, 'id': 1045}, {'country': b'Portugal', 'name': 'Ricardo Pacheco', 'nickname': b'fox', 'maps-played': 88, 'id': 629}, {'country': b'Sweden', 'name': 'Olof Kajbjer', 'nickname': b'olofmeister', 'maps-played': 533, 'id': 885}, {'country': b'Finland', 'name': 'Aleksi Jalli', 'nickname': b'allu', 'maps-played': 237, 'id': 695}, {'country': b'Norway', 'name': 'Joakim Myrbostad', 'nickname': b'jkaem', 'maps-played': 180, 'id': 8248}, {'country': b'Norway', 'name': 'Jorgen Robertsen', 'nickname': b'cromen', 'maps-played': 27, 'id': 10397}, {'country': b'Denmark', 'name': 'Philip Aistrup', 'nickname': b'aizy', 'maps-played': 218, 'id': 8095}, {'country': b'France', 'name': 'Fabien Fiey', 'nickname': b'kioShiMa', 'maps-played': 280, 'id': 4959}, {'country': b'Sweden', 'name': 'Robert Dahlström', 'nickname': b'RobbaN', 'maps-played': 2, 'id': 2}, {'country': b'Australia', 'name': 'Karlo Pivac', 'nickname': b'USTILO', 'maps-played': 1, 'id': 8771}, {'country': b'Denmark', 'name': 'Jesper Plougmann', 'nickname': b'TENZKI', 'maps-played': 2, 'id': 5287}, {'country': b'Serbia', 'name': 'Janko Paunović', 'nickname': b'YNk', 'maps-played': 8, 'id': 2482}, {'country': b'Sweden', 'name': 'Zebastian Molinder', 'nickname': b'zbM', 'maps-played': 1, 'id': 10748}], 'stats': {b'Maps played': b'994', b'Wins / draws / losses': b'567 / 5 / 422', b'Total kills': b'89743', b'Total deaths': b'85251', b'Rounds played': b'26101', b'K/D Ratio': b'1.05'}}
```

## `get_matches`  

```python
>>> hltv.get_matches()
[{'date': '2018-02-15', 'team1': 'SEAL', 'event': 'CSesport.com Cup #3', 'team2': 'Space Jam', 'time': '16:00'}, {'date': '2018-02-15', 'team1': 'fnatic', 'event': 'ESL Pro League Season 7 Europe', 'team2': 'NiP', 'time': '17:00'}, ... ]
```

## `get_results`

```python
>>> hltv.get_results()
[{'team2score': 16, 'team1': 'AGO', 'team2': 'G2', 'team1score': 8, 'date': '15/2/2018', 'event': 'ESL Pro League Season 7 Europe'}, ... ]
```

## `get_results_by_date`

```python
>>> hltv.get_results_by_date()
[{'team2score': 16, 'team1': 'AGO', 'team2': 'G2', 'team1score': 8, 'map': 'Inferno', 'date': '2018-2-15', 'event': 'ESL Pro League Season 7 Europe'}, ... ]
```
