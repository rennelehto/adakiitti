sql muutokset:
Delete from airport where name like "CLICK HERE%";
create table peli(
  ID int not null auto_increment,
  nimi varchar(40),
  primary key (ID)
);

insert into peli (nimi) values (Pelaaja);

insert into peli (nimi) values (Vastustaja);

create table highscore(
  ID int not null auto_increment,
  nimi varchar(40),
  score int(6),
  primary key (ID)
);

insert into highscore (nimi, score) values ("nimimerkki", "pisteet");
