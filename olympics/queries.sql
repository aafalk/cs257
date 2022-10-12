SELECT nocs.noc
FROM nocs
ORDER BY nocs.noc;

SELECT athletes.name, athletes.noc
FROM athletes
WHERE athletes.noc = 'JAM';

SELECT athletes.name, event_results.medal_id, games.year
FROM athletes, event_results, games
WHERE athletes.name = 'Greg Louganis'
AND athletes.id = event_results.athlete_id
AND event_results.medal_id != 'NA'
ORDER BY games.year;

SELECT medal_count.noc_id, medal_count.gold
FROM medal_count
ORDER BY medal_count.gold;
