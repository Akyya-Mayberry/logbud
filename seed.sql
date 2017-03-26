/***** Seeds data into logbud database *****/

/*
    To seed the data, change into directory where this
    file is located and run the command 'psql logbud < seed.sql'
*/

/* Create the tables. */
-- CREATE TABLE user_profiles (
--     id  integer PRIMARY KEY DEFAULT nextval('serial'),
--     email   varchar(100),
--     password    varchar(100),
-- );

-- CREATE TABLE visitors (
--     id    integer PRIMARY KEY DEFAULT nextval('serial'),
--     firstname   varchar(50),
--     lastname    varchar(50),

-- CREATE TABLE visits (
--     id integer PRIMARY KEY DEFAULT nextval('serial'),
--     visitor_id  integer,
--     visiting    varchar(100),
--     purpose varchar(100),
--     active
-- );

/* Authenticated user account with logging permissions */
INSERT INTO user_profiles VALUES (1, 'a@gmail.com', '');

/* Active Visitors */
INSERT INTO visitors VALUES (1, 'Mickey', 'Mouse');
INSERT INTO visitors VALUES (2, 'Donald', 'Duck');
INSERT INTO visitors VALUES (3, 'Daisy', 'Duck');
INSERT INTO visitors VALUES (4, 'Goofy', 'Dude');
INSERT INTO visitors VALUES (5, 'Pluto', 'Woof');
INSERT INTO visitors VALUES (6, 'Minnie', 'Mouse');

/* Recorded Visits */
INSERT INTO visits VALUES (1, 1, 'Color Crew', 'Practice learning his colors.', true);
INSERT INTO visits VALUES (2, 1, 'Color Crew', 'Practice learning his colors.', false);
INSERT INTO visits VALUES (3, 2, 'The Notekins', 'Work on his music pitch and tone.', true);
INSERT INTO visits VALUES (4, 3, 'Color Crew', 'Practice learning her colors.', true);
INSERT INTO visits VALUES (5, 3, 'Rainbow Horse', 'Comb rainbows hourse long colorful hair.', false);
INSERT INTO visits VALUES (6, 3, 'Suzy''s Zoo', 'Have fun with Zoo animals.', false);
INSERT INTO visits VALUES (7, 4, 'Tilly Knock Knock', 'Play knock knock with Tilly', false);
INSERT INTO visits VALUES (8, 5, 'Tilly Knock Knock', 'Play knock knock with Tilly', true);
INSERT INTO visits VALUES (9, 6, 'Color Crew', 'Practice learning his colors.', true);
INSERT INTO visits VALUES (10, 6, 'Rainbow Horse', 'Comb rainbows hourse long colorful hair.', false);
