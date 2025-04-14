CREATE TABLE messages IF NOT EXISTS (
    id int(11) NOT NULL AUTO_INCREMENT,
    content varchar(255) NOT NULL,
    updatetime Datetime NOT NULL,
    PRIMARY KEY (id)
);