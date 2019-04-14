CREATE TABLE IF NOT EXISTS lawsuitTable (
    id INT AUTO_INCREMENT,
    number varchar(255),
    judge_id int,
    courtsection_id int,
    disctrict_id int,
    kind_id int,
    FOREIGN KEY(judge_id) REFERENCES judgeTable(id),
    FOREIGN KEY(courtsection_id) REFERENCES courtsectionTable(id),
    FOREIGN KEY(disctrict_id) REFERENCES disctrictTable(id),
    FOREIGN KEY(kind_id) REFERENCES kindTable(id),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS lawsuitlawyerTable (
    id INT AUTO_INCREMENT,
    lawsuit_id INT,
    lawyer_id INT,
    FOREIGN KEY(lawsuit_id) REFERENCES lawsuitTable(id),
    FOREIGN KEY(lawyer_id) REFERENCES lawyerTable(id),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS lawsuitpersonTable (
    id INT AUTO_INCREMENT,
    lawsuit_id INT,
    person_id INT,
    FOREIGN KEY(lawsuit_id) REFERENCES lawsuitTable(id),
    FOREIGN KEY(person_id) REFERENCES personTable(id),
    PRIMARY KEY (id)
);
