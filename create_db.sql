CREATE TABLE person(
    tg_id VARCHAR(30) NOT NULL PRIMARY KEY,
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
    twenty_four_hour BOOLEAN,
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
    PRIMARY KEY(workday_id, post_id, person_id),
    FOREIGN KEY(workday_id) REFERENCES workday(id),
    FOREIGN KEY(post_id) REFERENCES post(id),
    FOREIGN KEY(person_id) REFERENCES person(tg_id),
);

INSERT INTO person(tg_id, first_name, last_name, mid_name, gender, birthday, age, is_admin boolean)
VALUES
    ('220697264', 'Денис', 'Смагин', 'Александрович', 'М', '1988-07-23', 34, TRUE);


INSERT INTO post(name, twenty_four_hour)
VALUES
    ('1/1', TRUE),
    ('1/2', TRUE),
    ('7/1', TRUE),
    ('7/1', TRUE),
    ('ГБР1', TRUE),
    ('ГБР2', TRUE),
    ('Ястреб', FALSE),
    ('Дежурный', TRUE),
    ('2', FALSE),
    ('3', FALSE);

