CREATE TABLE archery_events (
    Round VARCHAR(10),
    Division varchar(255), //FK
    Class varchar(255), FK
    PRIMARY KEY (Round, Division, Class),
    FOREIGN KEY (Division) REFERENCES Division(ACR),
    FOREIGN KEY (Class) REFERENCES Class(Id),
);