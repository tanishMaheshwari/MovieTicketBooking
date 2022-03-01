create database movieTicketBase;
use movieticketbooking;


CREATE TABLE userbase (
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
    movieDate date,
    timing VARCHAR(12),
    theatre VARCHAR(15),
    city VARCHAR(25),
    refreshment CHAR(1),
    foreign key (movieID) references moviebase(movieID),
    foreign key (userID) references userbase(userID)
);
CREATE TABLE moviebase(
	movieID int primary key not null auto_increment,
    name varchar(20),
    lastDate date,
    basePrice smallint,
    details varchar(50),
    ticketSold int
);