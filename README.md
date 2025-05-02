SQL-muutokset:

DELETE FROM airport WHERE name LIKE "CLICK HERE%";

CREATE TABLE peli 
(ID int NOT NULL auto_increment,
nimi varchar(40),
PRIMARY KEY (ID));

CREATE TABLE highscore
(nro int NOT NULL auto_increment,
ID varchar(40), 
pisteet int, 
PRIMARY KEY (nro), 
FOREIGN KEY (ID) REFERENCES peli (ID));
