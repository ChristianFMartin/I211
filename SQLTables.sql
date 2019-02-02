CREATE TABLE Songs
(songID int auto_increment,
Song varchar(50) NOT NULL,
Artist varchar(50),
Genre varchar(25),
Price decimal(2),
PRIMARY KEY(songID));

CREATE TABLE MyTunes
(MyTunesID int auto_increment,
SongID int,
PRIMARY KEY(MyTunesID));

INSERT INTO Songs
VALUES(1,'PYNK','Janelle Monae','Pop',1.99),
(2,'When Did Your Heart Go Missing?','Rooney','Rock',0.99),
(3,'Wake Me Up (Before You Go-Go)','Wham!','Pop',0.99),
(4,'Formation','Beyonce','R&B',2.99),
(5,'Pompeii','Bastille','Alternative',1.99);