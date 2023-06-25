
---

CREATE TABLE user_output.sessions_v2
(
  session_name varchar,
  aoi varchar,
  municipalities varchar,
  kt_table_name varchar,
  kv_table_name varchar,
  joli_table_name varchar,
  sid varchar PRIMARY KEY,
  usr varchar,
  starttime varchar(15),
  baseyear int2 NOT NULL,
  targetyear int2 NOT NULL,
  calculationScenario varchar,
  metodi varchar DEFAULT 'em',
  paastolaji varchar DEFAULT 'tuotanto'
);

GRANT SELECT, INSERT ON user_output.sessions_v2 TO ilmakalu_user;
GRANT SELECT ON user_output.sessions_v2 TO end_users;
