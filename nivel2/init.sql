CREATE TABLE country(
    id int NOT NULL auto_increment,
    country varchar(2),
    PRIMARY KEY (id)
);

CREATE TABLE city(
    id int NOT NULL auto_increment,
    city varchar(255),
    id_country int,
    PRIMARY KEY (id),
    active tinyint(1),
    FOREIGN KEY (id_country) REFERENCES country(id)
);

INSERT INTO `country` (`country`) VALUES ('NI');
INSERT INTO `country` (`country`) VALUES ('US');

INSERT INTO `city` (`city`, `id_country`, `active`) VALUES ('LEON', '1', '1');
INSERT INTO `city` (`city`, `id_country`, `active`) VALUES ('CHINANDEGA', '1', '0');
