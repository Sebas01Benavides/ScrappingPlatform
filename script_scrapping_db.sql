CREATE TABLE juegos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio NUMERIC(10,2),
    hash_datos TEXT NOT NULL,
    fuente TEXT
);

CREATE TABLE resultados_scraping (
    id SERIAL PRIMARY KEY,
    fuente TEXT,
    titulo TEXT,
    url_origen TEXT
);

CREATE TABLE logs_ejecucion (
    id SERIAL PRIMARY KEY,
    estado TEXT,
    mensaje TEXT
);


SELECT * FROM juegos;
SELECT * FROM resultados_scraping;
SELECT * FROM logs_ejecucion;