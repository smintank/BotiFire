INSERT INTO person(id, first_name, last_name, mid_name, gender, birthday, age, is_admin)
VALUES
    ('220697264', 'денис', 'смагин', 'александрович', 'м', '1988-07-23', 34, TRUE),
    ('501372585', 'антон', 'смагин', 'витальевич', 'м', '1990-03-13', 33, FALSE);

INSERT INTO post(name, alias, is_main, is_24h)
VALUES
    ('1_1', 'пост 1/1', TRUE, TRUE),
    ('1_2', 'пост 1/2', TRUE, TRUE),
    ('gbr1', 'Гбр 1', TRUE, TRUE),
    ('gbr2', 'Гбр 2', TRUE, TRUE),
    ('7_1', 'пост 7/1', TRUE, TRUE),
    ('7_2', 'пост 7/2', TRUE, TRUE),
    ('hawk', 'Ястреб', TRUE, FALSE),
    ('sentry', 'Дежурный', TRUE, TRUE),
    ('2', '2 пост', FALSE, FALSE),
    ('3', '3 пост', FALSE, FALSE);
