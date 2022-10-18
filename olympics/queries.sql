SELECT nocs.noc
FROM nocs
ORDER BY nocs.noc;

SELECT athletes.name, nocs.noc
FROM athletes, nocs
WHERE nocs.noc = 'JAM'
AND athletes.noc_id = nocs.id;

SELECT athletes.name, medals.medal, games.year
FROM event_results, athletes, medals, games
WHERE event_results.athlete_id = athletes.id
AND athletes.name = 'Gregory Efthimios "Greg" Louganis'
AND event_results.medal_id = medals.id
AND medals.medal != 'NA'
AND event_results.game_id = games.id
ORDER BY games.year;

SELECT medal_count.noc_id, medal_count.gold
FROM medal_count
ORDER BY medal_count.gold;
