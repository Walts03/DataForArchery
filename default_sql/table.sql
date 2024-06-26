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

