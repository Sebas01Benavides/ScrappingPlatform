-- =========================================
-- Script SQL completo - Plataforma de Scraping
-- Proyecto Computación en la Nube Sebas Benavides - UTN
-- =========================================

-- 1. Tabla de juegos (resultado principal del scraping dinámico)
CREATE TABLE IF NOT EXISTS juegos (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio NUMERIC(10,2),
    hash_datos TEXT NOT NULL,
    fuente TEXT,
    fecha_extraccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Tabla de resultados de scraping general (histórico de títulos extraídos)
CREATE TABLE IF NOT EXISTS resultados_scraping (
    id SERIAL PRIMARY KEY,
    fuente TEXT,
    titulo TEXT,
    url_origen TEXT,
    fecha_extraccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Tabla de logs de ejecución (historial del scheduler/main.py)
CREATE TABLE IF NOT EXISTS logs_ejecucion (
    id SERIAL PRIMARY KEY,
    estado TEXT,
    mensaje TEXT,
    fecha_ejecucion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================================
-- Consultas de verificación
-- =========================================

SELECT * FROM juegos ORDER BY id DESC;
SELECT * FROM resultados_scraping ORDER BY id DESC;
SELECT * FROM logs_ejecucion ORDER BY id DESC;