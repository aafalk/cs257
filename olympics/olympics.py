'''
    olympics.py
    Alex Falk, 19 Oct 2022

'''
import sys
import psycopg2
import config

def get_connection():
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()
    
def get_athletes(search_noc):
    ''' List the names of all the athletes from a specified NOC.'''
    athletes = []
    try:
        # Create a "cursor", which is an object with which you can iterate
        # over query results.
        connection = get_connection()
        cursor = connection.cursor()

        # Execute the query
        query = '''SELECT athletes.name FROM athletes, nocs WHERE nocs.noc = %s AND athletes.noc_id = nocs.id;'''
        cursor.execute(query, (search_noc,))

        # Iterate over the query results to produce the list of athlete names.
        for row in cursor:
            athlete_name = row[0]
            athletes.append(f'{athlete_name}')

    except Exception as e:
        print(e, file=sys.stderr)
    
    connection.close()
    return athletes

def get_golds():
    '''List all the NOCs and the number of gold medals they have won,
       in decreasing order of the number of gold medals.'''
    golds = []
    try:
        # Create a "cursor", which is an object with which you can iterate
        # over query results.
        connection = get_connection()
        cursor = connection.cursor()

        # Execute the query
        query = 'SELECT nocs.noc, medal_count.gold FROM medal_count, nocs WHERE medal_count.noc_id = nocs.id ORDER BY medal_count.gold DESC;'
        cursor.execute(query)

        # Iterate over the query results to produce the list of gold medal counts.
        for row in cursor:
            noc_name = row[0]
            gold_number = row[1]
            golds.append(f'{noc_name} {gold_number}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return golds

def get_games():
    '''List all the olympic games and their cities in the database ordered by year.'''
    games = []
    try:
        # Create a "cursor", which is an object with which you can iterate
        # over query results.
        connection = get_connection()
        cursor = connection.cursor()

        # Execute the query
        query = 'SELECT cities.city, seasons.season, games.year FROM cities, seasons, games WHERE games.city_id = cities.id AND games.season_id = seasons.id ORDER BY games.year;'
        cursor.execute(query)

        # Iterate over the query results to produce the list of gold medal counts.
        for row in cursor:
            city_name = row[0]
            season_name = row[1]
            year = row[2]
            games.append(f'{city_name} {season_name} {year}')

    except Exception as e:
        print(e, file=sys.stderr)
    
    connection.close()
    return games

def main():

    # Command line parsing
    if len(sys.argv) == 2 and (sys.argv[1] == 'golds' or sys.argv[1] == 'games'):
        if sys.argv[1] == 'golds':
            # Get a list of NOCs and their golds
            print(f'~~~~~~~~~~ NOCs and their Gold Medals ~~~~~~~~~~')
            golds = get_golds()
            for count in golds:
                print(count)
            print()
        else:
            # Get a list of olympic games, their city, and year
            print(f'~~~~~~~~~~ Olympic Games ~~~~~~~~~~')
            games = get_games()
            for years in games:
                print(years)
            print()
    elif len(sys.argv) == 3 and sys.argv[1] == 'athletes':
        # Get a list of athlete names
        input_noc = sys.argv[2]
        print('~~~~~~~~~~ Athletes from ' + input_noc + ' ~~~~~~~~~~')
        athletes = get_athletes(input_noc)
        for athlete in athletes:
            print(athlete)
        print()
    elif len(sys.argv) == 2 and sys.argv[0] == 'olympics.py' and sys.argv[1] == '-h':
        with open('usage.txt', 'r') as help_file:
            print(help_file.read())
    else:
        print('Usage error. For more information, please type: python3 olympics.py -h')
    
if __name__ == '__main__':
    main()
