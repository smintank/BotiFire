CREATE TABLE person(
    id VARCHAR(30) NOT NULL PRIMARY KEY,
    nickname VARCHAR(50),
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    mid_name VARCHAR(20),
    gender VARCHAR(1) DEFAULT 'M',
    birthday DATE,
    age INTEGER(2),
    is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE post(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    alias VARCHAR(50),
    is_main BOOLEAN NOT NULL,
    is_24h BOOLEAN,
    work_hours_amount INTEGER
);

CREATE TABLE workday(
    id INTEGER NOT NULL PRIMARY KEY,
    full_date DATE NOT NULL,
    cur_year INTEGER(4) NOT NULL,
    cur_month INTEGER(2) NOT NULL,
    is_holiday BOOLEAN,
    is_weekend BOOLEAN
);

CREATE TABLE day_post_user(
    workday_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    creator_id VARCHAR(30) NOT NULL,
    is_notified BOOLEAN DEFAULT FALSE,
    PRIMARY KEY(workday_id, post_id, person_id),
    FOREIGN KEY(workday_id) REFERENCES workday(id),
    FOREIGN KEY(post_id) REFERENCES post(id),
    FOREIGN KEY(person_id) REFERENCES person(id)
);

INSERT INTO person (id, first_name, last_name, mid_name, gender, birthday, age, is_admin)
VALUES
    ('220697264', 'денис', 'смагин', 'александрович', 'м', '1988-07-23', 34, TRUE),
    ('501372585', 'антон', 'смагин', 'витальевич', 'м', '1990-03-13', 33, FALSE);

INSERT INTO post (name, alias, is_main, is_24h)
VALUES
    ('1/1', '1 пост 1 смена', TRUE, TRUE),
    ('1/2', '1 пост 2 смена', TRUE, TRUE),
    ('ГБР1', 'Гбр 1', TRUE, TRUE),
    ('ГБР2', 'Гбр 2', TRUE, TRUE),
    ('7/1', '7 пост 1 смена',  TRUE, TRUE),
    ('7/2', '7 пост 2 смена', TRUE, TRUE),
    ('Яст', 'Ястреб', TRUE, FALSE),
    ('Деж', 'Дежурный', TRUE, TRUE),
    ('2', '2 пост', FALSE, FALSE),
    ('3', '3 пост', FALSE, FALSE);
