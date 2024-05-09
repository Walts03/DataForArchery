SELECT 
    CEIL(Arrow.Id / 6) AS EndNumber,
    ShootingSession.Id AS SessionId,
    Archer.Name,
    ShootingSession.CompetitionId,
    ShootingSession.RoundName,
    ShootingSession.Division,
    ShootingSession.Class,
    ShootingSession.SessionDate,
    GROUP_CONCAT(Arrow.Id) AS ArrowIds,
    MIN(Arrow.Dist) AS Distances,
    MIN(Arrow.ShootingRange) AS ShootingRanges,
    SUM(Arrow.Score) AS Scores,
    MIN(Arrow.ShootDate) AS ShootDates
FROM 
    ShootingSession
INNER JOIN 
    Arrow ON Arrow.ShootingSessionId = ShootingSession.Id
LEFT JOIN
    Archer ON ShootingSession.ArcherId = Archer.Id
WHERE 
    ShootingSession.Id = 1
GROUP BY 
    ShootingSession.Id,
    ShootingSession.ArcherId,
    ShootingSession.CompetitionId,
    ShootingSession.RoundName,
    ShootingSession.Division,
    ShootingSession.Class,
    ShootingSession.SessionDate,
    CEIL(Arrow.Id / 6);
