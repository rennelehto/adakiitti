SQL-muutokset:

DELETE FROM airport WHERE name LIKE "CLICK HERE%";

CREATE TABLE peli 
(ID int(10) NOT NULL auto_increment,
nimi varchar(40),
PRIMARY KEY (ID));

CREATE TABLE highscore
(nro int NOT NULL auto_increment,
ID int(10), 
pisteet int, 
PRIMARY KEY (nro), 
FOREIGN KEY (ID) REFERENCES peli (ID));

INSERT INTO peli (nimi) values ("Mörkö2");

INSERT INTO peli (nimi) values ("Haisuli");

INSERT INTO highscore (id, pisteet) VALUES ((SELECT id FROM peli WHERE nimi = "Mörkö2"), 666);

INSERT INTO highscore (id, pisteet) VALUES ((SELECT id FROM peli WHERE nimi = "Haisuli"), 616);
