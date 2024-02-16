create database project ;
use project;

CREATE TABLE persons (
  pname VARCHAR(255) NOT NULL,
  phone VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

INSERT INTO persons (pname, phone, email)
VALUES ('John Doe', '123-456-7890', 'johndoe@example.com');

select * from persons ;
