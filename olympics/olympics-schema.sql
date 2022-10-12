CREATE TABLE nocs (
    id SERIAL,
    noc text
);

CREATE TABLE athletes (
    id SERIAL,
    name text,
    sex_id integer,
    noc_id integer
);

CREATE TABLE seasons (
    id SERIAL,
    season text
);

CREATE TABLE cities (
    id SERIAL,
    city text
);

CREATE TABLE games (
    id SERIAL,
    game text,
    year integer,
    season_id integer,
    city_id integer
);

CREATE TABLE sports (
    id SERIAL,
    sport text
);

CREATE TABLE events (
    id SERIAL,
    event text,
    sport_id integer
);

CREATE TABLE medals (
    id SERIAL,
    medal text
);

CREATE TABLE event_results (
    athlete_id integer,
    game_id integer,
    event_id integer,
    medal_id integer
);

CREATE TABLE medal_count (
    noc_id integer
    gold integer
    silver integer
    bronze integer
);