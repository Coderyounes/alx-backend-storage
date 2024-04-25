-- SQL File Code Create Table user
DROP TABLE IF EXISTS users;
Create Table users (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255)
    country NOT NULL ENUM ('US', 'CO', 'TN') DEFAULT 1,
    PRIMARY KEY(id)
);
