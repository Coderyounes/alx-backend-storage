-- SQL File Code Create users Table in any Database
Create Table IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    PRIMARY KEY(id)
);
