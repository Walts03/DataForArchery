CREATE TABLE `Division` (
  Name varchar(255) NOT NULL,
  ACR varchar(255) NOT NULL,
  PRIMARY KEY (ACR)
);

INSERT INTO Division (Name, ACR) VALUES
('Recurve', 'R'),
('Compound', 'C'),
('Recurve/Compound Barebow', 'B'),
('Longbow', 'L');