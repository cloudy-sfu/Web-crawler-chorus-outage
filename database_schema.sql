--
-- PostgreSQL database dump
--

\restrict BTCBFQ96v6by6sERqRcKG4nsxiE64SZXtojtWYstib5f1NVDF3DAuNtXfAdUC5h

-- Dumped from database version 17.7 (bdc8956)
-- Dumped by pg_dump version 17.7

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

SET default_table_access_method = heap;

--
-- Name: chorus; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.chorus (
    start_time timestamp with time zone,
    incident_point jsonb,
    incident_area jsonb,
    role character varying(16),
    n_impacted_services smallint,
    description character varying(64),
    update_time timestamp with time zone,
    update_text text,
    recorded_time timestamp with time zone DEFAULT now()
);


--
-- Name: TABLE chorus; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.chorus IS 'This table records outages of New Zealand local fiber company Chorus.';


--
-- Name: COLUMN chorus.start_time; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.chorus.start_time IS 'The start time of outage.';


--
-- Name: COLUMN chorus.incident_point; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.chorus.incident_point IS 'The place of the label, which describes the incident, in chorus outage map. Values can be parsed by shapely.geometry.shape() Python function.';


--
-- Name: COLUMN chorus.incident_area; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.chorus.incident_area IS 'The area that cannot access to Internet. Values can be parsed by shapely.geometry.shape() Python function.';


--
-- Name: COLUMN chorus.n_impacted_services; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.chorus.n_impacted_services IS 'The number of Internet services that are impacted.';


--
-- Name: COLUMN chorus.update_time; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.chorus.update_time IS 'The publishing time of latest update about this incident.';


--
-- Name: COLUMN chorus.update_text; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.chorus.update_text IS 'The content of latest update about this incident.';


--
-- PostgreSQL database dump complete
--

\unrestrict BTCBFQ96v6by6sERqRcKG4nsxiE64SZXtojtWYstib5f1NVDF3DAuNtXfAdUC5h

