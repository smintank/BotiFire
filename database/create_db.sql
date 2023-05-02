CREATE TABLE rank(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    short_name VARCHAR(30) NOT NULL,
    is_officer BOOLEAN NOT NULL
);

CREATE TABLE employee(
    id VARCHAR(30) NOT NULL PRIMARY KEY,
    nickname VARCHAR(50),
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    mid_name VARCHAR(20),
    gender VARCHAR(1) DEFAULT 'M',
    birthday DATE,
    rank_id INTEGER NOT NULL,
    is_sentry BOOLEAN NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    FOREIGN KEY(rank_id) REFERENCES rank(id)
);

CREATE TABLE post(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    alias VARCHAR(50),
    ordering INTEGER NOT NULL,
    is_main BOOLEAN NOT NULL,
    is_24h BOOLEAN,
    work_hours_amount INTEGER
);

CREATE TABLE day_post_employee(
    workday_date DATE NOT NULL,
    post_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,
    is_notified BOOLEAN DEFAULT FALSE,
    PRIMARY KEY(workday_date, post_id, employee_id),
    FOREIGN KEY(post_id) REFERENCES post(id),
    FOREIGN KEY(employee_id) REFERENCES employee(id),
    FOREIGN KEY(creator_id) REFERENCES employee(id)
);
