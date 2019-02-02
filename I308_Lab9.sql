CREATE TABLE band 
(
bid INT AUTO_INCREMENT,
name VARCHAR(256),
year_formed YEAR, 
PRIMARY KEY(bid)
) ENGINE = INNODB;
INSERT INTO band
 VALUES 
(1, 'Red Hot Chili Peppers', 1983),

(2, 'Nirvana',1987),

(3, 'Veruca Salt', 1992)
,
(4, 'Spice Girls', 1994);




CREATE TABLE artist
(
aid INT AUTO_INCREMENT,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(100), 
dob DATE, 
gender VARCHAR(1), 
PRIMARY KEY(aid)
) ENGINE = INNODB; 


INSERT INTO artist 
VALUES 
(100, 'Anthony', 'Kiedis', '1962-11-01', 'M'),

(101, 'Mike B', 'the Flea', '1962-10-16', 'M'),

(102, 'Chad', 'Smith', '1961-10-25', 'M'),

(103, 'Josh', 'Klinghoffer', '1979-10-03', 'M'),

(104, 'Kurt', 'Cobain', '1967-02-20', 'M'),

(105, 'Krist', 'Novoselic', '1965-05-16', 'M'), 
(106, 'Dave', 'Grohl', '1969-01-14', 'M'),
(107, 'Louise', 'Post', '1966-12-07', 'F'),
(108, 'Nina', 'Gordon', '1967-11-14', 'F'),
(109, 'Jim', 'Shapiro', '1965-03-19', 'M'),
(110, 'Steve', 'Lack', '1969-07-15', 'M'),
(111, 'Melanie', 'Brown', '1975-05-29', 'F')
,
(112, 'Melanie', 'Chisholm', '1974-01-12', 'F')
,
(113, 'Emma', 'Bunton', '1976-01-21', 'F')
,
(114, 'Geri', 'Halliwell', '1972-08-06', 'F'),

(115, 'Victoria', 'Bekham', '1974-04-17', 'F');




CREATE TABLE in_band
(
aid INT NOT NULL, 
bid INT NOT NULL, 
date_in DATE NOT NULL, 
date_out DATE, 
FOREIGN KEY(aid) REFERENCES artist(aid),
FOREIGN KEY(bid) REFERENCES band(bid)
) ENGINE = INNODB;


INSERT INTO in_band 
VALUES 
(100, 1, '1983-12-01', NULL),

(101, 1, '1983-12-01', NULL),

(102, 1, '1988-07-03', NULL),

(103, 1, '2009-06-15', NULL),

(104, 2, '1987-03-17', '1994-07-01'),

(105, 2, '1987-03-17', '1994-07-05'),

(106, 2, '1987-03-17', '1994-07-05'),

(107, 3, '1992-05-30', NULL),

(108, 3, '1992-05-30', NULL),

(108, 4, '1994-04-25', NULL),

(109, 3, '1992-05-30', '1997-10-24'),

(109, 3, '2017-04-17', NULL),

(110, 3, '1992-05-30', NULL),

(111, 4, '1994-11-25', NULL),

(112, 4, '1994-11-25', NULL),

(113, 4, '1994-11-25', NULL),

(114, 4, '1994-11-25', NULL),

(115, 4, '1994-11-25', NULL);

CREATE TABLE album
(
albumid INT, 
bid INT NOT NULL,
published_year YEAR, 
title VARCHAR(256), 
price VARCHAR(50), 
publisher VARCHAR(200), 
format VARCHAR(10),
FOREIGN KEY(bid) REFERENCES band(bid)
) ENGINE = INNODB;



INSERT INTO album 
VALUES 
(200, 1, 1999, 'Californication', '$25.99', 'Warner Brothers', 'mp3'),

(201, 1, 2002, 'By The Way', '$25.99', 'Warner Brothers', 'mp3'),

(202, 1, 2006, 'Stadium Arcadium', '$25.99', 'Warner Brothers', 'mp3'),

(203, 2, 1991, 'Nevermind', '$30.00', 'DGC', 'mp3'),

(204, 3, 1994, 'American Thighs', '$20.00', 'DGC', 'mp3'),

(205, 3, 2000, 'Resolver', '$26.00', 'DGC', 'mp3'),

(206, 3, 2015, 'Ghost Notes', '$30.00', 'Warner Brothers', 'mp3'),

(207, 4, 1996, 'Spice', '$35.00', 'Virgin', 'mp3');






SELECT art.first_name, art.last_name, b.name
FROM artist as art, band as b, in_band as ib
WHERE art.aid = ib.aid
AND ib.bid=b.bid 
AND b.name ='Veruca Salt'; 


SELECT alb.title, art.first_name, art.last_name, b.name
FROM album as alb, in_band as ib, artist as art, band as b
WHERE ib.bid=alb.bid
AND ib.aid=art.aid
AND b.bid=ib.bid
AND alb.published_year BETWEEN ib.date_in AND ib.date_out OR ib.date_out = NULL;

SELECT CONCAT(art.first_name,," " art.last_name), DATE_FORMAT(art.dob, '%M %D, %Y') AS bday,TRUNCATE(DATEDIFF(CURDATE(), e.dob) /365.25) as age,b.name 
FROM artist as art, band as b, in_band as ib
WHERE art.gender='F'
AND ib.date_out IS NULL
HAVING age >=21;


