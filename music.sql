CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    name TEXT,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);

CREATE TABLE song (
    id INTEGER PRIMARY KEY,
    name TEXT,
    album_id INTEGER,
    track_number INTEGER,
    length_seconds INTEGER,
    FOREIGN KEY (album_id) REFERENCES album(id)
);
