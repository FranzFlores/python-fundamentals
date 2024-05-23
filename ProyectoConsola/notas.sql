CREATE DATABASE IF NOT EXISTS notes;
USE notes;

CREATE TABLE IF NOT EXISTS users (
    id INT(25) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    lastname VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    date DATE,
    CONSTRAINT pk_usuarios PRIMARY KEY (id),
    CONSTRAINT uq_email UNIQUE (email)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS notes (
    id INT(25) NOT NULL AUTO_INCREMENT,
    user_id INT(25) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description MEDIUMTEXT,
    date DATE,
    CONSTRAINT pk_notes PRIMARY KEY (id),
    CONSTRAINT fk_note_user FOREIGN KEY (user_id) REFERENCES users(id)
);