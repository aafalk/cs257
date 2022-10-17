""" 
    convert.py
    Alex Falk, 11 Oct 2022
    
"""
import csv

# CREATE TABLE nocs (
#     id SERIAL
#     noc text
# );
nocs = {}
with open('noc_regions.csv') as original_data_file, open('nocs.csv', 'w') as nocs_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(nocs_file, lineterminator = '\n')
    heading_row = next(reader)
    for row in reader:
        noc_name = row[0]
        if noc_name == 'SIN': # Singapore check
            noc_name = 'SGP'
        if noc_name not in nocs:
            noc_id = len(nocs) + 1
            nocs[noc_name] = noc_id
            writer.writerow([noc_id, noc_name])

# CREATE TABLE sexes (
#     id SERIAL
#     sex text
# );
sexes = {}
with open('sexes.csv', 'w') as sexes_file:
    writer = csv.writer(sexes_file, lineterminator = '\n')
    sexes['M'] = 1
    sexes['F'] = 2
    for key in sexes:
        writer.writerow([sexes[key], key])
    

# CREATE TABLE athletes (
#     id SERIAL
#     name text
#     sex_id integer
#     noc_id integer
# );
athletes = {}
with open('athlete_events.csv') as original_data_file, open('athletes.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file, lineterminator = '\n')
    heading_row = next(reader)
    for row in reader:
        athlete_id = row[0]
        athlete_name = row[1]
        sex_id = sexes[row[2]]
        noc_id = nocs[row[7]]
        if athlete_name not in athletes:
            athletes[athlete_name] = athlete_id
            writer.writerow([athlete_id, athlete_name, sex_id, noc_id])

# CREATE TABLE seasons (
#     id SERIAL
#     season text
# );
seasons = {}
with open('seasons.csv', 'w') as seasons_file:
    writer = csv.writer(seasons_file, lineterminator = '\n')
    seasons['Summer'] = 1
    seasons['Winter'] = 2
    for key in seasons:
        writer.writerow([seasons[key], key])
    

# CREATE TABLE cities (
#     id SERIAL
#     city text
# );
cities = {}
with open('athlete_events.csv') as original_data_file, open('cities.csv', 'w') as cities_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(cities_file, lineterminator = '\n')
    heading_row = next(reader)
    for row in reader:
        city_name = row[11]
        if city_name not in cities:
            city_id = len(cities) + 1
            cities[city_name] = city_id
            writer.writerow([city_id, city_name])

# CREATE TABLE games (
#     id SERIAL
#     game text
#     year integer
#     season_id integer
#     city_id integer
# );
games = {}
with open('athlete_events.csv') as original_data_file, open('games.csv', 'w') as games_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(games_file, lineterminator = '\n')
    heading_row = next(reader)
    for row in reader:
        game_name = row[8]
        game_year = row[9]
        season_id = seasons[row[10]]
        city_id = cities[row[11]]
        if game_name not in games:
            game_id = len(games) + 1
            games[game_name] = game_id
            writer.writerow([game_id, game_name, game_year, season_id, city_id])

# CREATE TABLE sports (
#     id SERIAL
#     sport text
# );
sports = {}
with open('athlete_events.csv') as original_data_file, open('sports.csv', 'w') as sports_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(sports_file, lineterminator = '\n')
    heading_row = next(reader)
    for row in reader:
        sport_name = row[12]
        if sport_name not in sports:
            sport_id = len(sports) + 1
            sports[sport_name] = sport_id
            writer.writerow([sport_id, sport_name])

# CREATE TABLE events (
#     id SERIAL
#     event text
#     sport_id integer
# );
events = {}
with open('athlete_events.csv') as original_data_file, open('events.csv', 'w') as events_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(events_file, lineterminator = '\n')
    heading_row = next(reader)
    for row in reader:
        event_name = row[13]
        sport_id = sports[row[12]]
        if event_name not in events:
            event_id = len(events) + 1
            events[event_name] = event_id
            writer.writerow([event_id, event_name, sport_id])

# CREATE TABLE medals (
#     id SERIAL
#     medal text
# );
medals = {}
with open('medals.csv', 'w') as medals_file:
    writer = csv.writer(medals_file, lineterminator = '\n')
    medals['Gold'] = 1
    medals['Silver'] = 2
    medals['Bronze'] = 3
    medals['NA'] = 4
    for key in medals:
        writer.writerow([medals[key], key])

# CREATE TABLE event_results (
#     athlete_id integer
#     game_id integer
#     event_id integer
#     medal_id integer
# );
with open('athlete_events.csv') as original_data_file, open('event_results.csv', 'w') as event_results_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(event_results_file, lineterminator = '\n')
    heading_row = next(reader)
    for row in reader:
        athlete_id = athletes[row[1]]
        game_id = games[row[8]]
        event_id = events[row[13]]
        medal_id = medals[row[14]]
        writer.writerow([athlete_id, game_id, event_id, medal_id])

# CREATE TABLE medal_count (
#     noc_id integer
#     gold integer
#     silver integer
#     bronze integer
# );
medal_count = {}
with open('athlete_events.csv') as original_data_file, open('medal_count.csv', 'w') as medal_count_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(medal_count_file, lineterminator = '\n')
    heading_row = next(reader)
    gold = 0
    silver = 0
    bronze = 0
    for row in reader:
        noc_id = nocs[row[7]]        
        if noc_id not in medal_count:
            medal_count[noc_id] = [gold, silver, bronze]
        else:
            prev_gold = medal_count[noc_id][0]
            prev_silver = medal_count[noc_id][1]
            prev_bronze = medal_count[noc_id][2]
            if row[14] == 'Gold':
                medal_count[noc_id] = [prev_gold + 1, prev_silver, prev_bronze]
            elif row[14] == 'Silver':
                medal_count[noc_id] = [prev_gold, prev_silver + 1, prev_bronze]
            elif row[14] == 'Bronze':
                medal_count[noc_id] = [prev_gold, prev_silver, prev_bronze + 1]
    for key in medal_count:
        writer.writerow([key, medal_count[key][0], medal_count[key][1], medal_count[key][2]])
