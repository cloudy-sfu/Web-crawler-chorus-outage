create table public.chorus
(
    start_time          timestamp with time zone,
    incident_point      jsonb,
    incident_area       jsonb,
    role                varchar(16),
    n_impacted_services smallint,
    description         varchar(64),
    update_time         timestamp with time zone,
    update_text         text,
    recorded_time       timestamp with time zone default now()
);

comment on table public.chorus is 'This table records outages of New Zealand local fiber company Chorus.';

comment on column public.chorus.start_time is 'The start time of outage.';

comment on column public.chorus.incident_point is 'The place of the label, which describes the incident, in chorus outage map. Values can be parsed by shapely.geometry.shape() Python function.';

comment on column public.chorus.incident_area is 'The area that cannot access to Internet. Values can be parsed by shapely.geometry.shape() Python function.';

comment on column public.chorus.n_impacted_services is 'The number of Internet services that are impacted.';

comment on column public.chorus.update_time is 'The publishing time of latest update about this incident.';

comment on column public.chorus.update_text is 'The content of latest update about this incident.';

alter table public.chorus
    owner to neondb_owner;

