DROP TABLE IF EXISTS Arrow;
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
	Name VARCHAR(255),
	DOB DATETIME,
	Gender VARCHAR(255),
	DefaultDivision VARCHAR(255),
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
	Name varchar(255) NOT NULL,
	ACR varchar(255) NOT NULL,
	PRIMARY KEY (ACR)
);

CREATE TABLE Class (
	Name VARCHAR(255) NOT NULL,
	PRIMARY KEY (Name)
);


CREATE TABLE Round (
	Name VARCHAR(255),
	Equivalent VARCHAR(255) NULL,
	MaxScoreByArrow INT,
	PRIMARY KEY (Name),
	FOREIGN KEY (Equivalent) REFERENCES Round(Name)
);

CREATE TABLE SubRound (
	Dist INT,
	ShootingRange INT,
	TargetFace INT,
	RoundName VARCHAR(255),
	PRIMARY KEY (Dist, ShootingRange, TargetFace, RoundName),
	FOREIGN KEY (TargetFace) REFERENCES TargetFace(Size),
	FOREIGN KEY (Dist) REFERENCES Distance(Dist),
	FOREIGN KEY (ShootingRange) REFERENCES ShootingRange(EndNo),
	FOREIGN KEY (RoundName) REFERENCES Round(Name)
);

CREATE TABLE Competition (
	Id INT	NOT NULL AUTO_INCREMENT,
	IsChampionship BOOLEAN,
	Name VARCHAR(255),
	Duration INT,
	CompetitionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (Id)
);

CREATE TABLE ShootingSession (
	Id INT NOT NULL AUTO_INCREMENT,
	ArcherId INT,
	CompetitionId INT,
	RoundName VARCHAR(255),
	Division VARCHAR(255),
	Class VARCHAR(255),
	SessionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (Id),
	FOREIGN KEY (ArcherId) REFERENCES Archer(Id),
	FOREIGN KEY (CompetitionId) REFERENCES Competition(Id),
	FOREIGN KEY (Division) REFERENCES Division(ACR),
	FOREIGN KEY (RoundName) REFERENCES Round(Name)
);

CREATE TABLE Arrow (
	Id INT NOT NULL AUTO_INCREMENT,
	Dist INT,
	ShootingRange INT,
	ShootingSessionId INT,
	Score INT,
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
(5);
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
(TRUE, 'Archery Australia Championship', '2024-06-20');

INSERT INTO Archer (Name, DOB, Gender, DefaultDivision) VALUES
('Richard Ortiz', '1992-04-04', 'Female', 'R'),
('Thomas Young', '1981-03-05', 'Male', 'C'),
('Vicki Pennington', '1988-08-24', 'Female', 'B'),
('Jenna Proctor', '1975-10-21', 'Female', 'L'),
('Stephanie Cain', '1993-03-03', 'Female', 'L'),
('Rebecca Wilson', '1968-01-20', 'Female', 'B'),
('Glen Gonzalez', '1989-02-03', 'Female', 'B'),
('Judith Davis', '1967-12-29', 'Male', 'R'),
('Steven Davis', '1984-11-10', 'Female', 'R'),
('Katherine Schultz', '2000-12-11', 'Male', 'L');
