from datetime import datetime, timedelta

rounds_dict = [{
    'WA90/1440': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (90, 6): {
                'TargetFace': 80,
                'ShootingRange': 6
            },
            (70, 6): {
                'TargetFace': 80,
                'ShootingRange': 6
            },
            (50, 6): {
                'TargetFace': 120,
                'ShootingRange': 6
            },
            (30, 6): {
                'TargetFace': 120,
                'ShootingRange': 6
            }
        }
    },
    'WA70/1440': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (70, 6): {
                'TargetFace': 80,
                'ShootingRange': 6
            },
            (60, 6): {
                'TargetFace': 80,
                'ShootingRange': 6
            },
            (50, 6): {
                'TargetFace': 120,
                'ShootingRange': 6
            },
            (30, 6): {
                'TargetFace': 120,
                'ShootingRange': 6
            }
        }
    },
    'WA60/1440': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (60, 6): {
                'TargetFace': 80,
                'ShootingRange': 6
            },
            (50, 6): {
                'TargetFace': 80,
                'ShootingRange': 6
            },
            (40, 6): {
                'TargetFace': 120,
                'ShootingRange': 6
            },
            (30, 6): {
                'TargetFace': 120,
                'ShootingRange': 6
            }
        }
    },
}, {
    'AA50/1440': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (50, 6): {
                'TargetFace': 80,
                'ShootingRange': 6
            },
            (40, 6): {
                'TargetFace': 80,
                'ShootingRange': 6
            },
            (30, 6): {
                'TargetFace': 120,
                'ShootingRange': 6
            },
            (20, 6): {
                'TargetFace': 120,
                'ShootingRange': 6
            }
        }
    },
    'AA40/1440': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (40, 6): {
                'TargetFace': 80,
                'ShootingRange': 6
            },
            (30, 6): {
                'TargetFace': 80,
                'ShootingRange': 6
            },
            (20, 6): {
                'TargetFace': 120,
                'ShootingRange': 6
            }
        }
    },
    'Long Sydney': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (90, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (70, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (60, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (50, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            }
        }
    },
    'Sydney': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (70, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (60, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (50, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (40, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            }
        }
    },
    'Long Brisbane': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (90, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (70, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (60, 5): {
                'TargetFace': 120,
                'ShootingRange': 5
            },
            (50, 5): {
                'TargetFace': 120,
                'ShootingRange': 5
            }
        }
    },
    'Brisbane': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (70, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (60, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (50, 5): {
                'TargetFace': 120,
                'ShootingRange': 5
            },
            (40, 5): {
                'TargetFace': 120,
                'ShootingRange': 5
            }
        }
    },
    'Adelaide': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (60, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (50, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (40, 5): {
                'TargetFace': 120,
                'ShootingRange': 5
            },
            (30, 5): {
                'TargetFace': 120,
                'ShootingRange': 5
            }
        }
    },
    'Hobart': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (90, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (70, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (50, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            }
        }
    },
    'Perth': {
        'EquivalentRound': None,
        'MaxScoreByArrow': 10,
        'SubRounds': {
            (70, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (60, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            },
            (50, 5): {
                'TargetFace': 80,
                'ShootingRange': 5
            }
        }
    }
}]

# Dictionary for competitions
competitions = [{
    'Id': 1,
    'IsChampionship': True,
    'Name': 'World Archery 2190',
    'CompetitionDate': '2024-04-15',
    'Duration': 7
}, {
    'Id': 2,
    'IsChampionship': False,
    'Name': 'Archery Australia Championship',
    'CompetitionDate': '2024-06-20',
    'Duration': 5
}]

shoot_hour = [7, 10, 13, 16]

archer = [
    {
        "Division": "R",
        "Class": "50+ Male",
    },
    {
        "Division": "C",
        "Class": "Female Open",
    },
    {
        "Division": "B",
        "Class": "Male Open",
    },
    {
        "Division": "L",
        "Class": "50+ Male",
    },
]

import random


# Helper function to generate random shoot time within the specified range
def generate_shoot_time():
    return random.randint(10, 15)


# Helper function to generate random score for an arrow within the range of 0 to max score
def generate_arrow_score(max_score):
    return random.randint(0, max_score)


shooting_session = 1

for id, competition in enumerate(competitions):
    competition_date = datetime.strptime(competition['CompetitionDate'],
                                         '%Y-%m-%d')
    for day in range(competition['Duration']):
        for hour in shoot_hour:
            session_date = competition_date.replace(hour=hour)
            for archer_id in range(1, 5):
                round_name = random.choice(list(rounds_dict[id].keys()))
                round_data = rounds_dict[id][round_name]
                max_score = round_data['MaxScoreByArrow']
                shoot_date = session_date
                print(
                    f"INSERT INTO ShootingSession (ArcherId, CompetitionId, RoundName, SessionDate, Class, Division) "
                    f"VALUES ({archer_id}, {competition['Id']}, '{round_name}', '{shoot_date.strftime('%Y-%m-%d %H:%M:%S')}', '{archer[archer_id - 1]['Class']}', '{archer[archer_id - 1]['Division']}');"
                )
                # Insert Arrows
                for dist_shooting_range, sub_round_data in round_data[
                        'SubRounds'].items():
                    dist, shooting_range = dist_shooting_range
                    target_face = sub_round_data['TargetFace']
                    for _ in range(shooting_range):
                        for _ in range(6):
                            score = generate_arrow_score(max_score)
                            print(
                                f"INSERT INTO Arrow (Dist, ShootingRange, ShootingSessionId, Score, ShootDate) "
                                f"VALUES ({dist}, {shooting_range}, {shooting_session}, {score}, "
                                f"'{shoot_date.strftime('%Y-%m-%d %H:%M:%S')}');"
                            )

                            shoot_time = generate_shoot_time()
                            shoot_date += timedelta(minutes=shoot_time)
                shooting_session += 1
