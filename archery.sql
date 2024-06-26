DROP TABLE IF EXISTS End;
DROP TABLE IF EXISTS ShootingSession;
DROP TABLE IF EXISTS Archer;
DROP TABLE IF EXISTS Competition;
DROP TABLE IF EXISTS SubRound;
DROP TABLE IF EXISTS TargetFace;
DROP TABLE IF EXISTS Distance;
DROP TABLE IF EXISTS Division;
DROP TABLE IF EXISTS Class;
DROP TABLE IF EXISTS ShootingRange;
DROP TABLE IF EXISTS Round;

CREATE TABLE Archer (
  Id INT NOT NULL AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  DOB DATETIME NOT NULL,
  Gender VARCHAR(255) NOT NULL,
  DefaultDivision VARCHAR(255) NOT NULL,
  PRIMARY KEY (Id)
);

CREATE TABLE TargetFace (
  Size INT PRIMARY KEY
);

CREATE TABLE Distance (
  Dist INT PRIMARY KEY
);

CREATE TABLE ShootingRange (
  EndNo INT PRIMARY KEY
);

CREATE TABLE Division (
  Name VARCHAR(255) NOT NULL,
  ACR VARCHAR(255) NOT NULL,
  PRIMARY KEY (ACR)
);

CREATE TABLE Class (
  Name VARCHAR(255) NOT NULL,
  PRIMARY KEY (Name)
);

CREATE TABLE Round (
  Name VARCHAR(255) NOT NULL,
  Equivalent VARCHAR(255) NULL,
  MaxScoreByArrow INT NOT NULL,
  PRIMARY KEY (Name),
  FOREIGN KEY (Equivalent) REFERENCES Round(Name)
);

CREATE TABLE SubRound (
  Dist INT NOT NULL,
  ShootingRange INT NOT NULL,
  TargetFace INT NOT NULL,
  RoundName VARCHAR(255) NOT NULL,
  PRIMARY KEY (Dist, ShootingRange, TargetFace, RoundName),
  FOREIGN KEY (TargetFace) REFERENCES TargetFace(Size),
  FOREIGN KEY (Dist) REFERENCES Distance(Dist),
  FOREIGN KEY (ShootingRange) REFERENCES ShootingRange(EndNo),
  FOREIGN KEY (RoundName) REFERENCES Round(Name)
);

CREATE TABLE Competition (
  Id INT NOT NULL AUTO_INCREMENT,
  IsChampionship BOOLEAN NOT NULL,
  Name VARCHAR(255) UNIQUE NOT NULL,
  Duration INT NOT NULL,
  CompetitionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (Id)
);

CREATE TABLE ShootingSession (
  Id INT NOT NULL AUTO_INCREMENT,
  ArcherId INT NOT NULL,
  CompetitionId INT NOT NULL,
  RoundName VARCHAR(255) NOT NULL,
  Division VARCHAR(255) NOT NULL,
  Class VARCHAR(255) NOT NULL,
  SessionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (Id),
  FOREIGN KEY (ArcherId) REFERENCES Archer(Id),
  FOREIGN KEY (CompetitionId) REFERENCES Competition(Id),
  FOREIGN KEY (Division) REFERENCES Division(ACR),
  FOREIGN KEY (RoundName) REFERENCES Round(Name)
);

CREATE TABLE End (
  Id INT NOT NULL AUTO_INCREMENT,
  ShootingSessionId INT NOT NULL,
  Dist INT NOT NULL,
  ShootingRange INT NOT NULL,
  Arrow1 INT NOT NULL,
  Arrow2 INT NOT NULL,
  Arrow3 INT NOT NULL,
  Arrow4 INT NOT NULL,
  Arrow5 INT NOT NULL,
  Arrow6 INT NOT NULL,
  ShootDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (Id),
  FOREIGN KEY (Dist) REFERENCES Distance(Dist),
  FOREIGN KEY (ShootingRange) REFERENCES ShootingRange(EndNo),
  FOREIGN KEY (ShootingSessionId) REFERENCES ShootingSession(Id)
);


INSERT INTO Class (Name) VALUES 
('Female Open'),
('Male Open'),
('50+ Female'),
('50+ Male'),
('60+ Female'),
('60+ Male'),
('70+ Female'),
('70+ Male'),
('Under 21 Female'),
('Under 21 Male'),
('Under 18 Female'),
('Under 18 Male'),
('Under 16 Female'),
('Under 16 Male'),
('Under 14 Female'),
('Under 14 Male');

INSERT INTO Distance (Dist) VALUES
(90),
(70),
(60),
(50),
(40),
(30),
(20);

INSERT INTO Division (Name, ACR) VALUES
('Recurve', 'R'),
('Compound', 'C'),
('Recurve/Compound Barebow', 'B'),
('Longbow', 'L');

INSERT INTO ShootingRange (EndNo) VALUES
(6),
(5),
(3);

INSERT INTO Round (Name, MaxScoreByArrow) VALUES
('WA90/1440', 10),
('WA70/1440', 10),
('WA60/1440', 10),
('AA50/1440', 10),
('AA40/1440', 10),
('Long Sydney', 10),
('Sydney', 10),
('Long Brisbane', 10),
('Brisbane', 10),
('Adelaide', 10),
('Short Adelaide', 10),
('Hobart', 10),
('Perth', 10);

INSERT INTO Round (Name, MaxScoreByArrow, Equivalent) VALUES
('WA60/1440 - Children', 10, 'WA60/1440');

INSERT INTO TargetFace (Size) VALUES
(120),
(80);

INSERT INTO SubRound (Dist, ShootingRange, RoundName, TargetFace) VALUES
(90, 6, 'WA90/1440', 80),
(70, 6, 'WA90/1440', 80),
(50, 6, 'WA90/1440', 120),
(30, 6, 'WA90/1440', 120),
(70, 6, 'WA70/1440', 80),
(60, 6, 'WA70/1440', 80),
(50, 6, 'WA70/1440', 120),
(30, 6, 'WA70/1440', 120),
(60, 6, 'WA60/1440', 80),
(50, 6, 'WA60/1440', 80),
(40, 6, 'WA60/1440', 120),
(30, 6, 'WA60/1440', 120),
(40, 3, 'WA60/1440 - Children', 120),
(30, 3, 'WA60/1440 - Children', 120),
(50, 6, 'AA50/1440', 80),
(40, 6, 'AA50/1440', 80),
(30, 6, 'AA50/1440', 120),
(20, 6, 'AA50/1440', 120),
(40, 6, 'AA40/1440', 80),
(30, 6, 'AA40/1440', 80),
(30, 6, 'AA40/1440', 120),
(20, 6, 'AA40/1440', 120),
(90, 5, 'Long Sydney', 80),
(70, 5, 'Long Sydney', 80),
(60, 5, 'Long Sydney', 80),
(50, 5, 'Long Sydney', 80),
(70, 5, 'Sydney', 80),
(60, 5, 'Sydney', 80),
(50, 5, 'Sydney', 80),
(40, 5, 'Sydney', 80),
(90, 5, 'Long Brisbane', 80),
(70, 5, 'Long Brisbane', 80),
(60, 5, 'Long Brisbane', 120),
(50, 5, 'Long Brisbane', 120),
(70, 5, 'Brisbane', 80),
(60, 5, 'Brisbane', 80),
(50, 5, 'Brisbane', 120),
(40, 5, 'Brisbane', 120),
(60, 5, 'Adelaide', 80),
(50, 5, 'Adelaide', 80),
(40, 5, 'Adelaide', 120),
(30, 5, 'Adelaide', 120),
(90, 5, 'Hobart', 80),
(70, 5, 'Hobart', 80),
(50, 5, 'Hobart', 80),
(70, 5, 'Perth', 80),
(60, 5, 'Perth', 80),
(50, 5, 'Perth', 80);

INSERT INTO Competition (IsChampionship, Name, CompetitionDate) VALUES
(TRUE, 'World Archery 2190', '2024-04-15'),
(TRUE, 'Archery Australia Championship', '2024-06-20'),
(FALSE, 'Staging', '2020-01-01');

