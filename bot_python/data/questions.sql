-- SQLite
DROP TABLE questions;

CREATE TABLE questions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  question TEXT NOT NULL,
  data_type TEXT NOT NULL,
  required TEXT NOT NULL,
  answered BOOL NOT NULL DEFAULT 0
);

INSERT INTO questions (question, data_type, required, answered) VALUES ("How many cars are in Bolzano?", "number of cars", "photo,position", 0);
INSERT INTO questions (question, data_type, required, answered) VALUES ("How many bikes are around yourself?", "number of bikes", "photo,position", 0);
INSERT INTO questions (question, data_type, required, answered) VALUES ("How crowded is it?", "number of persons", "mult", 0);

DELETE FROM questions where id > 0;

SELECT * FROM questions;