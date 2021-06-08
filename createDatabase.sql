create database movieTicketBase;

create table userBase;
create table ticketBase;
create table movieBase;

CREATE TABLE userBase (
	userID SMALLINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    age SMALLINT UNSIGNED NOT NULL,
    gender CHAR(1) NOT NULL,
    phoneNumber VARCHAR(13),
    email VARCHAR(50),
    city VARCHAR(20) NOT NULL
);

CREATE TABLE ticketBase(
	ticketID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    movieID SMALLINT ,
	userID SMALLINT,
    seatType varchar(20),
    movieDate varchar(10),
    timing VARCHAR(12),
    theatre VARCHAR(15),
    city VARCHAR(25),
    refreshment CHAR(1)
);
CREATE TABLE ticketbase(
	movieID int primary key not null auto_increment,
    name varchar(20),
    lastDate varchar(10),
    basePrice smallint,
    details varchar(50),
    ticketSold int
    );