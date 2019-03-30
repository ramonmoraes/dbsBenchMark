CREATE TABLE IF NOT EXISTS lawsuitTable (
    id INT AUTO_INCREMENT,
    number varchar(255),
    judge FOREIGN KEY REFERENCES judgeTable(id),
    courtsection FOREIGN KEY REFERENCES courtsectionTable(id),
    disctrict FOREIGN KEY REFERENCES disctrictTable(id),
    subject FOREIGN KEY REFERENCES subjectTable(id),
    kind FOREIGN KEY REFERENCES kindTable(id),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS lawsuitlawyersTable (
    id INT AUTO_INCREMENT,
    lawsuit_id FOREIGN KEY REFERENCES lawsuitTable(id)
    lawyer_id FOREIGN KEY REFERENCES lawyerTable(id)
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS personTable (
    id INT AUTO_INCREMENT,
    lawsuit_id FOREIGN KEY REFERENCES lawsuitTable(id)
    person_id FOREIGN KEY REFERENCES personTable(id)
    PRIMARY KEY (id)
);
