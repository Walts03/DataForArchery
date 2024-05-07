INSERT INTO ShootingRange (EndNo) VALUES
(6),
(5);

INSERT INTO Division (Name, ACR) VALUES
('Recurve', 'R'),
('Compound', 'C'),
('Recurve/Compound Barebow', 'B'),
('Longbow', 'L');

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

INSERT INTO Archer (Name, DOB, Gender, DefaultDivision) VALUES
('Robin Hood', '1980-12-13', 'Male', 'R'),
('Katniss Everdeen', '1992-05-08', 'Female', 'C'),
('Legolas', '1400-03-29', 'Male', 'B'),
('Hawkeye', '1972-09-18', 'Male', 'L');

INSERT INTO Competition (IsChampionship, Name, CompetitionDate) VALUES
(TRUE, 'World Archery 2190', '2024-04-15'),
(TRUE, 'Archery Australia Championship', '2024-06-20');
