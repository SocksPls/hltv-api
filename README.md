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
['karrigan', 'olofmeister', 'GuardiaN', 'NiKo', 'rain']
```

## `get_team_info`  

```python
>>> hltv.get_team_info("6667")
{'stats': {'Maps played': '466', 'K/D Ratio': '1.06', 'Total deaths': '40328', 'Wins / draws / losses': '279 / 1 / 186', 'Total kills': '42711', 'Rounds played': '12212'}, 'current-lineup': [{'maps-played': 314, 'country': 'Denmark', 'nickname': 'karrigan', 'name': 'Finn Andersen'}, {'maps-played': 141, 'country': 'Sweden', 'nickname': 'olofmeister', 'name': 'Olof Kajbjer'}, {'maps-played': 141, 'country': 'Slovakia', 'nickname': 'GuardiaN', 'name': 'Ladislav Kov\xc3\xa1cs'}, {'maps-played': 237, 'country': 'Bosnia and Herzegovina', 'nickname': 'NiKo', 'name': 'Nikola Kova\xc4\x8d'}, {'maps-played': 466, 'country': 'Norway', 'nickname': 'rain', 'name': 'H\xc3\xa5vard Nygaard'}], 'team-name': 'FaZe', 'historical-players': [{'maps-played': 25, 'country': 'Sweden', 'nickname': 'Maikelele', 'name': 'Mikail Bill'}, {'maps-played': 88, 'country': 'Portugal', 'nickname': 'fox', 'name': 'Ricardo Pacheco'}, {'maps-played': 237, 'country': 'Finland', 'nickname': 'allu', 'name': 'Aleksi Jalli'}, {'maps-played': 180, 'country': 'Norway', 'nickname': 'jkaem', 'name': 'Joakim Myrbostad'}, {'maps-played': 218, 'country': 'Denmark', 'nickname': 'aizy', 'name': 'Philip Aistrup'}, {'maps-played': 280, 'country': 'France', 'nickname': 'kioShiMa', 'name': 'Fabien Fiey'}, {'maps-played': 2, 'country': 'Sweden', 'nickname': 'RobbaN', 'name': 'Robert Dahlstr\xc3\xb6m'}, {'maps-played': 2, 'country': 'Denmark', 'nickname': 'TENZKI', 'name': 'Jesper Plougmann'}, {'maps-played': 1, 'country': 'Sweden', 'nickname': 'zbM', 'name': 'Zebastian Molinder'}]}
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
