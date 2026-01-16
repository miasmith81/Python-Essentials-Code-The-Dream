-- ═══════════════════════════════════════════════════════════════════════════════
-- 📊 Week 6: SQL & Databases - Test Database Schema
-- Code the Dream - Python Essentials
-- ═══════════════════════════════════════════════════════════════════════════════
-- This SQL file creates a complete test database for learning SQL fundamentals.
-- Topics covered: CREATE TABLE, INSERT, SELECT, WHERE, JOIN, GROUP BY, ORDER BY
-- ═══════════════════════════════════════════════════════════════════════════════

-- ═══════════════════════════════════════════════════════════════════════════════
-- SECTION 1: Music Albums Database
-- ═══════════════════════════════════════════════════════════════════════════════

-- Drop tables if they exist (for re-running the script)
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS tracks;
DROP TABLE IF EXISTS playlists;
DROP TABLE IF EXISTS playlist_tracks;

-- Create artists table (one-to-many relationship with albums)
CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(50),
    formed_year INTEGER,
    genre VARCHAR(50)
);

-- Create albums table with foreign key to artists
CREATE TABLE albums (
    album_id INTEGER PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    artist_id INTEGER NOT NULL,
    release_year INTEGER,
    genre VARCHAR(50),
    total_tracks INTEGER,
    duration_minutes REAL,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

-- Create tracks table (one-to-many relationship with albums)
CREATE TABLE tracks (
    track_id INTEGER PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    album_id INTEGER NOT NULL,
    track_number INTEGER,
    duration_seconds INTEGER,
    FOREIGN KEY (album_id) REFERENCES albums(album_id)
);

-- Create playlists table
CREATE TABLE playlists (
    playlist_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_date TEXT DEFAULT CURRENT_DATE
);

-- Create junction table for many-to-many relationship (playlists ↔ tracks)
CREATE TABLE playlist_tracks (
    playlist_id INTEGER NOT NULL,
    track_id INTEGER NOT NULL,
    position INTEGER,
    added_date TEXT DEFAULT CURRENT_DATE,
    PRIMARY KEY (playlist_id, track_id),
    FOREIGN KEY (playlist_id) REFERENCES playlists(playlist_id),
    FOREIGN KEY (track_id) REFERENCES tracks(track_id)
);

-- ═══════════════════════════════════════════════════════════════════════════════
-- SECTION 2: Insert Sample Data - Artists
-- ═══════════════════════════════════════════════════════════════════════════════

INSERT INTO artists (artist_id, name, country, formed_year, genre) VALUES
(1, 'The Beatles', 'UK', 1960, 'Rock'),
(2, 'Michael Jackson', 'USA', 1964, 'Pop'),
(3, 'Pink Floyd', 'UK', 1965, 'Progressive Rock'),
(4, 'AC/DC', 'Australia', 1973, 'Hard Rock'),
(5, 'Fleetwood Mac', 'UK', 1967, 'Rock'),
(6, 'Queen', 'UK', 1970, 'Rock'),
(7, 'Led Zeppelin', 'UK', 1968, 'Hard Rock'),
(8, 'Taylor Swift', 'USA', 2004, 'Pop'),
(9, 'Kendrick Lamar', 'USA', 2003, 'Hip Hop'),
(10, 'Daft Punk', 'France', 1993, 'Electronic');

-- ═══════════════════════════════════════════════════════════════════════════════
-- SECTION 3: Insert Sample Data - Albums
-- ═══════════════════════════════════════════════════════════════════════════════

INSERT INTO albums (album_id, title, artist_id, release_year, genre, total_tracks, duration_minutes) VALUES
(1, 'Abbey Road', 1, 1969, 'Rock', 17, 47.5),
(2, 'Thriller', 2, 1982, 'Pop', 9, 42.3),
(3, 'The Dark Side of the Moon', 3, 1973, 'Progressive Rock', 10, 43.0),
(4, 'Back in Black', 4, 1980, 'Hard Rock', 10, 42.1),
(5, 'Rumours', 5, 1977, 'Rock', 11, 39.5),
(6, 'A Night at the Opera', 6, 1975, 'Rock', 12, 43.1),
(7, 'Led Zeppelin IV', 7, 1971, 'Hard Rock', 8, 42.5),
(8, '1989', 8, 2014, 'Pop', 13, 48.6),
(9, 'DAMN.', 9, 2017, 'Hip Hop', 14, 55.0),
(10, 'Random Access Memories', 10, 2013, 'Electronic', 13, 74.3),
(11, 'Sgt. Peppers Lonely Hearts Club Band', 1, 1967, 'Rock', 13, 40.0),
(12, 'Bad', 2, 1987, 'Pop', 11, 48.2),
(13, 'The Wall', 3, 1979, 'Progressive Rock', 26, 81.0),
(14, 'Folklore', 8, 2020, 'Indie Folk', 16, 63.3);

-- ═══════════════════════════════════════════════════════════════════════════════
-- SECTION 4: Insert Sample Data - Tracks (Sample from key albums)
-- ═══════════════════════════════════════════════════════════════════════════════

INSERT INTO tracks (track_id, title, album_id, track_number, duration_seconds) VALUES
-- Abbey Road tracks
(1, 'Come Together', 1, 1, 260),
(2, 'Something', 1, 2, 182),
(3, 'Here Comes the Sun', 1, 7, 185),
-- Thriller tracks
(4, 'Wanna Be Startin Somethin', 2, 1, 363),
(5, 'Thriller', 2, 4, 357),
(6, 'Beat It', 2, 5, 258),
(7, 'Billie Jean', 2, 6, 294),
-- Dark Side of the Moon tracks
(8, 'Speak to Me', 3, 1, 68),
(9, 'Breathe', 3, 2, 169),
(10, 'Time', 3, 4, 413),
(11, 'Money', 3, 6, 382),
-- 1989 tracks
(12, 'Welcome to New York', 8, 1, 212),
(13, 'Blank Space', 8, 2, 231),
(14, 'Shake It Off', 8, 6, 219),
(15, 'Bad Blood', 8, 8, 211),
-- DAMN. tracks
(16, 'DNA.', 9, 2, 185),
(17, 'HUMBLE.', 9, 8, 177),
(18, 'LOVE.', 9, 10, 213);

-- ═══════════════════════════════════════════════════════════════════════════════
-- SECTION 5: Insert Sample Data - Playlists
-- ═══════════════════════════════════════════════════════════════════════════════

INSERT INTO playlists (playlist_id, name, description, created_date) VALUES
(1, 'Classic Rock Essentials', 'The best of 60s and 70s rock', '2024-01-15'),
(2, 'Workout Mix', 'High energy tracks for the gym', '2024-02-01'),
(3, 'Chill Vibes', 'Relaxing tunes for studying', '2024-02-10'),
(4, 'Pop Hits 2010s', 'Chart toppers from the decade', '2024-03-01');

INSERT INTO playlist_tracks (playlist_id, track_id, position, added_date) VALUES
-- Classic Rock Essentials
(1, 1, 1, '2024-01-15'),  -- Come Together
(1, 2, 2, '2024-01-15'),  -- Something
(1, 3, 3, '2024-01-15'),  -- Here Comes the Sun
(1, 10, 4, '2024-01-15'), -- Time
(1, 11, 5, '2024-01-15'), -- Money
-- Workout Mix
(2, 6, 1, '2024-02-01'),  -- Beat It
(2, 14, 2, '2024-02-01'), -- Shake It Off
(2, 16, 3, '2024-02-01'), -- DNA.
(2, 17, 4, '2024-02-01'), -- HUMBLE.
-- Pop Hits 2010s
(4, 12, 1, '2024-03-01'), -- Welcome to New York
(4, 13, 2, '2024-03-01'), -- Blank Space
(4, 14, 3, '2024-03-01'), -- Shake It Off
(4, 17, 4, '2024-03-01'); -- HUMBLE.

-- ═══════════════════════════════════════════════════════════════════════════════
-- SECTION 6: Sales Data Table (For aggregation practice)
-- ═══════════════════════════════════════════════════════════════════════════════

DROP TABLE IF EXISTS album_sales;

CREATE TABLE album_sales (
    sale_id INTEGER PRIMARY KEY,
    album_id INTEGER NOT NULL,
    sale_date TEXT NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price REAL NOT NULL,
    region VARCHAR(50),
    format VARCHAR(20),  -- 'CD', 'Vinyl', 'Digital', 'Streaming'
    FOREIGN KEY (album_id) REFERENCES albums(album_id)
);

INSERT INTO album_sales (sale_id, album_id, sale_date, quantity, unit_price, region, format) VALUES
(1, 1, '2024-01-05', 2, 14.99, 'North America', 'Vinyl'),
(2, 2, '2024-01-07', 1, 9.99, 'Europe', 'CD'),
(3, 3, '2024-01-10', 3, 19.99, 'North America', 'Vinyl'),
(4, 8, '2024-01-12', 5, 12.99, 'Asia', 'Digital'),
(5, 9, '2024-01-15', 2, 11.99, 'North America', 'Digital'),
(6, 1, '2024-01-18', 1, 9.99, 'Europe', 'CD'),
(7, 2, '2024-01-20', 4, 0.99, 'North America', 'Streaming'),
(8, 5, '2024-01-22', 2, 14.99, 'Europe', 'Vinyl'),
(9, 6, '2024-01-25', 1, 12.99, 'Asia', 'CD'),
(10, 10, '2024-01-28', 3, 15.99, 'Europe', 'Vinyl'),
(11, 8, '2024-02-01', 10, 0.99, 'North America', 'Streaming'),
(12, 9, '2024-02-03', 7, 0.99, 'Europe', 'Streaming'),
(13, 2, '2024-02-05', 2, 9.99, 'Asia', 'CD'),
(14, 3, '2024-02-08', 1, 24.99, 'North America', 'Vinyl'),
(15, 4, '2024-02-10', 3, 12.99, 'Europe', 'CD'),
(16, 7, '2024-02-12', 2, 19.99, 'North America', 'Vinyl'),
(17, 11, '2024-02-15', 1, 14.99, 'Asia', 'Vinyl'),
(18, 12, '2024-02-18', 4, 8.99, 'Europe', 'Digital'),
(19, 13, '2024-02-20', 2, 29.99, 'North America', 'Vinyl'),
(20, 14, '2024-02-22', 6, 11.99, 'Asia', 'Digital');

-- ═══════════════════════════════════════════════════════════════════════════════
-- SECTION 7: Practice Queries (Run these to test your understanding!)
-- ═══════════════════════════════════════════════════════════════════════════════

-- Basic SELECT queries
-- Query 1: List all albums
SELECT * FROM albums;

-- Query 2: Select specific columns
SELECT title, release_year, genre FROM albums;

-- Query 3: Filter with WHERE
SELECT * FROM albums WHERE release_year > 1980;

-- Query 4: Sort with ORDER BY
SELECT title, release_year FROM albums ORDER BY release_year DESC;

-- Query 5: Count records
SELECT COUNT(*) AS total_albums FROM albums;

-- ═══════════════════════════════════════════════════════════════════════════════
-- SECTION 8: JOIN Queries
-- ═══════════════════════════════════════════════════════════════════════════════

-- Query 6: INNER JOIN - Albums with artist names
SELECT 
    albums.title AS album_title,
    artists.name AS artist_name,
    albums.release_year
FROM albums
INNER JOIN artists ON albums.artist_id = artists.artist_id
ORDER BY albums.release_year;

-- Query 7: JOIN with filtering
SELECT 
    artists.name,
    albums.title,
    albums.genre
FROM albums
INNER JOIN artists ON albums.artist_id = artists.artist_id
WHERE artists.country = 'UK';

-- Query 8: Multiple JOINs - Tracks with album and artist info
SELECT TOP 10
    tracks.title AS track_title,
    albums.title AS album_title,
    artists.name AS artist_name,
    tracks.duration_seconds
FROM tracks
INNER JOIN albums ON tracks.album_id = albums.album_id
INNER JOIN artists ON albums.artist_id = artists.artist_id
ORDER BY tracks.duration_seconds DESC;

-- ═══════════════════════════════════════════════════════════════════════════════
-- SECTION 9: Aggregation Queries (GROUP BY)
-- ═══════════════════════════════════════════════════════════════════════════════

-- Query 9: Count albums per artist
SELECT 
    artists.name,
    COUNT(albums.album_id) AS album_count
FROM artists
LEFT JOIN albums ON artists.artist_id = albums.artist_id
GROUP BY artists.artist_id
ORDER BY album_count DESC;

-- Query 10: Average album duration by genre
SELECT 
    genre,
    COUNT(*) AS num_albums,
    ROUND(AVG(duration_minutes), 1) AS avg_duration,
    MIN(release_year) AS earliest,
    MAX(release_year) AS latest
FROM albums
GROUP BY genre
ORDER BY num_albums DESC;

-- Query 11: Total sales by region
SELECT 
    region,
    COUNT(*) AS num_sales,
    SUM(quantity) AS total_units,
    ROUND(SUM(quantity * unit_price), 2) AS total_revenue
FROM album_sales
GROUP BY region
ORDER BY total_revenue DESC;

-- Query 12: Best selling albums
SELECT 
    albums.title,
    artists.name,
    SUM(album_sales.quantity) AS units_sold,
    ROUND(SUM(album_sales.quantity * album_sales.unit_price), 2) AS revenue
FROM album_sales
INNER JOIN albums ON album_sales.album_id = albums.album_id
INNER JOIN artists ON albums.artist_id = artists.artist_id
GROUP BY albums.album_id
ORDER BY revenue DESC;

-- ═══════════════════════════════════════════════════════════════════════════════
-- SECTION 10: HAVING Clause (Filter after GROUP BY)
-- ═══════════════════════════════════════════════════════════════════════════════

-- Query 13: Genres with more than 2 albums
SELECT 
    genre,
    COUNT(*) AS album_count
FROM albums
GROUP BY genre
HAVING album_count > 2
ORDER BY album_count DESC;

-- Query 14: Artists with total album duration over 80 minutes
SELECT 
    artists.name,
    SUM(albums.duration_minutes) AS total_duration
FROM artists
INNER JOIN albums ON artists.artist_id = albums.artist_id
GROUP BY artists.artist_id
HAVING total_duration > 80
ORDER BY total_duration DESC;