-- This is a sample for creating db


DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS planetvotes;


CREATE TABLE users 
(
    id              SERIAL PRIMARY KEY,
    username        CHARACTER VARYING(255) NOT NULL,
    email           CHARACTER VARYING(255) NOT NULL,
    password        CHARACTER VARYING(255) NOT NULL
);


CREATE TABLE planetvotes 
(
    id               SERIAL PRIMARY KEY,
    planet_id        TEXT,
    planet_name      CHARACTER VARYING(255) NOT NULL,
    user_id          INTEGER,
    submission_time  DATE,

    CONSTRAINT fk_users FOREIGN KEY (user_id) REFERENCES users(id)

);
