CREATE TABLE IF NOT EXISTS personTable (
    id INT AUTO_INCREMENT,
    name varchar(255),last_name varchar(255),
    PRIMARY KEY (id)
);CREATE TABLE IF NOT EXISTS lawyerTable (
    id INT AUTO_INCREMENT,
    name varchar(255),last_name varchar(255),is_lawyer boolean,
    PRIMARY KEY (id)
);CREATE TABLE IF NOT EXISTS judgeTable (
    id INT AUTO_INCREMENT,
    name varchar(255),last_name varchar(255),is_judge boolean,
    PRIMARY KEY (id)
);CREATE TABLE IF NOT EXISTS kindTable (
    id INT AUTO_INCREMENT,
    name varchar(255),
    PRIMARY KEY (id)
);CREATE TABLE IF NOT EXISTS courtsectionTable (
    id INT AUTO_INCREMENT,
    name varchar(255),
    PRIMARY KEY (id)
);CREATE TABLE IF NOT EXISTS disctrictTable (
    id INT AUTO_INCREMENT,
    name varchar(255),estate varchar(255),
    PRIMARY KEY (id)
);CREATE TABLE IF NOT EXISTS subjectTable (
    id INT AUTO_INCREMENT,
    name varchar(255),
    PRIMARY KEY (id)
);