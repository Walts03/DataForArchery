CREATE INDEX idx_archer_name ON Archer(Name);

CREATE INDEX idx_competition_name ON Competition(Name);
CREATE INDEX idx_competition_ischampionship ON Competition(IsChampionship);
CREATE INDEX idx_competition_date ON Competition(CompetitionDate);

CREATE INDEX idx_shootingsession_archer_competition ON ShootingSession(ArcherId, CompetitionId);
CREATE INDEX idx_shootingsession_roundname ON ShootingSession(RoundName);
CREATE INDEX idx_shootingsession_id ON ShootingSession(Id);
CREATE INDEX idx_shootingsession_competition_class ON ShootingSession(CompetitionId, Class);

CREATE INDEX idx_subround_distance_range ON SubRound(Dist, ShootingRange);

CREATE INDEX idx_arrow_session_distance_range ON Arrow(ShootingSessionId, Dist, ShootingRange);
