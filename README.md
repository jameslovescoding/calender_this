# calender_this
Python Flask practice project

CREATE TABLE appointments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(200) NOT NULL,
  start_datetime TIMESTAMP NOT NULL,
  end_datetime TIMESTAMP NOT NULL,
  description VARCHAR NOT NULL,
  private BOOLEAN NOT NULL
);

INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
VALUES
(
  'My appointment',
  '2023-07-20 14:00:00',
  '2023-07-20 15:00:00',
  'An appointment for me',
  false
);