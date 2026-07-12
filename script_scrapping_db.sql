
-- 1. Tabla para almacenar la información extraída (Scraping)
CREATE TABLE IF NOT EXISTS resultados_scraping (
    id SERIAL PRIMARY KEY,
    fuente VARCHAR(100),            -- Ejemplo: 'Wikipedia' o 'Sitio X'
    titulo TEXT,                    -- El contenido que extraes
    url_origen VARCHAR(255),        -- De dónde vino el dato
    fecha_extraccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Tabla para registrar los logs o historial de ejecuciones
CREATE TABLE IF NOT EXISTS logs_ejecucion (
    id SERIAL PRIMARY KEY,
    fecha_ejecucion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(50),             -- Ejemplo: 'EXITO' o 'ERROR'
    mensaje TEXT                    -- Detalles adicionales
);
-- 3. Tabla para juegos
CREATE TABLE IF NOT EXISTS juegos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio decimal(10,2)
);

ALTER TABLE juegos ADD COLUMN hash_datos VARCHAR(255);

SELECT * FROM juegos;