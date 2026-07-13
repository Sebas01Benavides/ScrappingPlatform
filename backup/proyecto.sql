--
-- PostgreSQL database dump
--

\restrict c93G8sVOJge6w4odyBLcjTkbFzsvT69LoRjjaBml145aKD8Lhd5BM4A62gj6Y66

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: juegos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.juegos (
    id integer NOT NULL,
    nombre text NOT NULL,
    precio numeric(10,2),
    hash_datos text NOT NULL,
    fuente text,
    fecha_extraccion timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.juegos OWNER TO postgres;

--
-- Name: juegos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.juegos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.juegos_id_seq OWNER TO postgres;

--
-- Name: juegos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.juegos_id_seq OWNED BY public.juegos.id;


--
-- Name: logs_ejecucion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.logs_ejecucion (
    id integer NOT NULL,
    estado text,
    mensaje text,
    fecha_ejecucion timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.logs_ejecucion OWNER TO postgres;

--
-- Name: logs_ejecucion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.logs_ejecucion_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.logs_ejecucion_id_seq OWNER TO postgres;

--
-- Name: logs_ejecucion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.logs_ejecucion_id_seq OWNED BY public.logs_ejecucion.id;


--
-- Name: resultados_scraping; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resultados_scraping (
    id integer NOT NULL,
    fuente text,
    titulo text,
    url_origen text,
    fecha_extraccion timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.resultados_scraping OWNER TO postgres;

--
-- Name: resultados_scraping_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.resultados_scraping_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.resultados_scraping_id_seq OWNER TO postgres;

--
-- Name: resultados_scraping_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resultados_scraping_id_seq OWNED BY public.resultados_scraping.id;


--
-- Name: juegos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juegos ALTER COLUMN id SET DEFAULT nextval('public.juegos_id_seq'::regclass);


--
-- Name: logs_ejecucion id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.logs_ejecucion ALTER COLUMN id SET DEFAULT nextval('public.logs_ejecucion_id_seq'::regclass);


--
-- Name: resultados_scraping id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resultados_scraping ALTER COLUMN id SET DEFAULT nextval('public.resultados_scraping_id_seq'::regclass);


--
-- Data for Name: juegos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.juegos (id, nombre, precio, hash_datos, fuente, fecha_extraccion) FROM stdin;
16	Discord Nitro - 3 Month TRIAL Subscription Key GLOBAL	0.54	9ce760be20dc487075b44959e266123b3fc5255308dd1e6517d0223e25c0e857	https://www.eneba.com/discord-discord-nitro-3-month-trial-subscription-key-global	2026-07-12 22:13:10.999516
17	2400 Call of Duty: Modern Warfare Points (Xbox One) Xbox Live Key GLOBAL	5.12	24f420404813310be1cc944fa75c6dab65844812a67bfbea5fc593f99d8e7cd3	https://www.eneba.com/xbox-2400-call-of-duty-modern-warfare-points-xbox-one-xbox-live-key-global	2026-07-12 22:13:10.999516
18	Top Up Poppo Live Coins	0.29	1a025c571657e00c26d8e32e3810af6fbaeaedab912aacd76ed1b2ccd98ad441	https://www.eneba.com/top-up-poppo-live-coins-global	2026-07-12 22:13:10.999516
19	Discord Nitro - 1 Month TRIAL Subscription Key GLOBAL	0.32	8112435d248e2e766f6f2b94598f5b4ecd85d703866cfe57ae8cf830358cb1e5	https://www.eneba.com/discord-discord-nitro-1-month-trial-subscription-key-global	2026-07-12 22:13:10.999516
20	Minecraft: Java & Bedrock Edition (PC) Official website Key GLOBAL	34.22	c558825bdc000de72c5d05abfee7af25ecd5d683deeba61a222a060ae420e6ac	https://www.eneba.com/other-minecraft-java-bedrock-edition-pc-official-website-key-global	2026-07-12 22:13:10.999516
21	Razer Gold Gift Card 5 USD Key GLOBAL	4.68	2c3b120a2e0dc7a745c3af6fb0f4c610fc35fe64929cd935df468ecab8182baa	https://www.eneba.com/razer-razer-gold-gift-card-5-usd-key-global	2026-07-12 22:13:10.999516
22	Xbox Game Pass Ultimate – 1 Month Subscription (Xbox/Windows) Non-stackable Key GLOBAL	14.82	4f68ef590a4cd3d8e9ab4de29c4b3ee19db9bd6e41a147276227a78a4ee98eb2	https://www.eneba.com/xbox-xbox-game-pass-ultimate-1-month-subscription-xbox-windows-non-stackable-key-global	2026-07-12 22:13:10.999516
23	Grand Theft Auto V Rockstar Games Launcher Key GLOBAL	34.22	da38ec3fddf4a508d09d975fbf4c2b5106794d656bce4ba9146f32cfa5bc720a	https://www.eneba.com/rockstar-social-club-grand-theft-auto-v-gta-rockstar-social-club-key-global	2026-07-12 22:13:10.999516
\.


--
-- Data for Name: logs_ejecucion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.logs_ejecucion (id, estado, mensaje, fecha_ejecucion) FROM stdin;
1	EXITO	Proceso completado: insertado	2026-07-12 21:08:30.20475
2	EXITO	Proceso completado: sin_cambios	2026-07-12 21:08:30.20475
3	EXITO	Proceso completado: actualizado	2026-07-12 21:08:30.20475
4	EXITO	Proceso completado: sin_cambios	2026-07-12 21:08:30.20475
5	EXITO	Proceso completado: actualizado	2026-07-12 21:08:30.20475
6	EXITO	Proceso completado: actualizado	2026-07-12 21:30:10.819483
7	EXITO	Proceso completado: sin_cambios	2026-07-12 21:30:42.843512
8	EXITO	Proceso completado. Registros procesados: 10	2026-07-12 21:45:57.406017
9	EXITO	Proceso completado. Registros procesados: 0	2026-07-12 21:48:40.216903
10	EXITO	Proceso completado. Registros procesados: 4	2026-07-12 21:53:41.384347
11	EXITO	Proceso completado. Registros procesados: 0	2026-07-12 22:03:52.434359
12	EXITO	Proceso completado. Registros procesados: 8	2026-07-12 22:13:10.999516
13	EXITO	Proceso completado. Registros procesados: 8	2026-07-12 22:18:51.026533
\.


--
-- Data for Name: resultados_scraping; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.resultados_scraping (id, fuente, titulo, url_origen, fecha_extraccion) FROM stdin;
22	https://www.eneba.com/discord-discord-nitro-3-month-trial-subscription-key-global	Discord Nitro - 3 Month TRIAL Subscription Key GLOBAL	https://www.eneba.com/discord-discord-nitro-3-month-trial-subscription-key-global	2026-07-12 22:13:10.999516
23	https://www.eneba.com/xbox-2400-call-of-duty-modern-warfare-points-xbox-one-xbox-live-key-global	2400 Call of Duty: Modern Warfare Points (Xbox One) Xbox Live Key GLOBAL	https://www.eneba.com/xbox-2400-call-of-duty-modern-warfare-points-xbox-one-xbox-live-key-global	2026-07-12 22:13:10.999516
24	https://www.eneba.com/top-up-poppo-live-coins-global	Top Up Poppo Live Coins	https://www.eneba.com/top-up-poppo-live-coins-global	2026-07-12 22:13:10.999516
25	https://www.eneba.com/discord-discord-nitro-1-month-trial-subscription-key-global	Discord Nitro - 1 Month TRIAL Subscription Key GLOBAL	https://www.eneba.com/discord-discord-nitro-1-month-trial-subscription-key-global	2026-07-12 22:13:10.999516
26	https://www.eneba.com/other-minecraft-java-bedrock-edition-pc-official-website-key-global	Minecraft: Java & Bedrock Edition (PC) Official website Key GLOBAL	https://www.eneba.com/other-minecraft-java-bedrock-edition-pc-official-website-key-global	2026-07-12 22:13:10.999516
27	https://www.eneba.com/razer-razer-gold-gift-card-5-usd-key-global	Razer Gold Gift Card 5 USD Key GLOBAL	https://www.eneba.com/razer-razer-gold-gift-card-5-usd-key-global	2026-07-12 22:13:10.999516
28	https://www.eneba.com/xbox-xbox-game-pass-ultimate-1-month-subscription-xbox-windows-non-stackable-key-global	Xbox Game Pass Ultimate – 1 Month Subscription (Xbox/Windows) Non-stackable Key GLOBAL	https://www.eneba.com/xbox-xbox-game-pass-ultimate-1-month-subscription-xbox-windows-non-stackable-key-global	2026-07-12 22:13:10.999516
29	https://www.eneba.com/rockstar-social-club-grand-theft-auto-v-gta-rockstar-social-club-key-global	Grand Theft Auto V Rockstar Games Launcher Key GLOBAL	https://www.eneba.com/rockstar-social-club-grand-theft-auto-v-gta-rockstar-social-club-key-global	2026-07-12 22:13:10.999516
30	https://www.eneba.com/discord-discord-nitro-3-month-trial-subscription-key-global	Discord Nitro - 3 Month TRIAL Subscription Key GLOBAL	https://www.eneba.com/discord-discord-nitro-3-month-trial-subscription-key-global	2026-07-12 22:18:51.026533
31	https://www.eneba.com/xbox-2400-call-of-duty-modern-warfare-points-xbox-one-xbox-live-key-global	2400 Call of Duty: Modern Warfare Points (Xbox One) Xbox Live Key GLOBAL	https://www.eneba.com/xbox-2400-call-of-duty-modern-warfare-points-xbox-one-xbox-live-key-global	2026-07-12 22:18:51.026533
32	https://www.eneba.com/top-up-poppo-live-coins-global	Top Up Poppo Live Coins	https://www.eneba.com/top-up-poppo-live-coins-global	2026-07-12 22:18:51.026533
33	https://www.eneba.com/discord-discord-nitro-1-month-trial-subscription-key-global	Discord Nitro - 1 Month TRIAL Subscription Key GLOBAL	https://www.eneba.com/discord-discord-nitro-1-month-trial-subscription-key-global	2026-07-12 22:18:51.026533
34	https://www.eneba.com/other-minecraft-java-bedrock-edition-pc-official-website-key-global	Minecraft: Java & Bedrock Edition (PC) Official website Key GLOBAL	https://www.eneba.com/other-minecraft-java-bedrock-edition-pc-official-website-key-global	2026-07-12 22:18:51.026533
35	https://www.eneba.com/razer-razer-gold-gift-card-5-usd-key-global	Razer Gold Gift Card 5 USD Key GLOBAL	https://www.eneba.com/razer-razer-gold-gift-card-5-usd-key-global	2026-07-12 22:18:51.026533
36	https://www.eneba.com/xbox-xbox-game-pass-ultimate-1-month-subscription-xbox-windows-non-stackable-key-global	Xbox Game Pass Ultimate – 1 Month Subscription (Xbox/Windows) Non-stackable Key GLOBAL	https://www.eneba.com/xbox-xbox-game-pass-ultimate-1-month-subscription-xbox-windows-non-stackable-key-global	2026-07-12 22:18:51.026533
37	https://www.eneba.com/rockstar-social-club-grand-theft-auto-v-gta-rockstar-social-club-key-global	Grand Theft Auto V Rockstar Games Launcher Key GLOBAL	https://www.eneba.com/rockstar-social-club-grand-theft-auto-v-gta-rockstar-social-club-key-global	2026-07-12 22:18:51.026533
\.


--
-- Name: juegos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.juegos_id_seq', 23, true);


--
-- Name: logs_ejecucion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.logs_ejecucion_id_seq', 13, true);


--
-- Name: resultados_scraping_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resultados_scraping_id_seq', 37, true);


--
-- Name: juegos juegos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.juegos
    ADD CONSTRAINT juegos_pkey PRIMARY KEY (id);


--
-- Name: logs_ejecucion logs_ejecucion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.logs_ejecucion
    ADD CONSTRAINT logs_ejecucion_pkey PRIMARY KEY (id);


--
-- Name: resultados_scraping resultados_scraping_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resultados_scraping
    ADD CONSTRAINT resultados_scraping_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict c93G8sVOJge6w4odyBLcjTkbFzsvT69LoRjjaBml145aKD8Lhd5BM4A62gj6Y66

