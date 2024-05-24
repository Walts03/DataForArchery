from datetime import datetime, timedelta
import json

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
	# 'WA60/1440 - Children': {
	# 	'EquivalentRound': 'WA60/1440',
	# 	'MaxScoreByArrow': 10,
	# 	'SubRounds': {
	# 		(40, 3): {
	# 			'TargetFace': 120,
	# 			'ShootingRange': 3
	# 		},
	# 		(30, 3): {
	# 			'TargetFace': 120,
	# 			'ShootingRange': 3
	# 		}
	# 	}
	# },
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

shoot_hour = [7, 10, 13, 16]

def calculate_age(dob):
	today = datetime.today()
	dob = datetime.strptime(dob, '%Y-%m-%d')  # Convert string to datetime
	age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
	return age

def classify_archer(age, gender):
	# Define the classes based on age and gender
	if age < 14:
		return f'Under 14 {gender}'
	elif age < 16:
		return f'Under 16 {gender}'
	elif age < 18:
		return f'Under 18 {gender}'
	elif age < 21:
		return f'Under 21 {gender}'
	elif age < 50:
		return f'{gender} Open'
	elif age < 60:
		return f'50+ {gender}'
	elif age < 70:
		return f'60+ {gender}'
	else:
		return f'70+ {gender}'

with open('generated_data/archers.json', 'r') as json_file:
	archers = json.load(json_file)

# Process each archer to calculate age and determine their class
for i, archer in enumerate(archers):
	age = calculate_age(archer['DOB'])
	archers[i]['Class'] = classify_archer(age, archer['Gender'])

# archer = archers[0:299]
archer = archers[:10]

import random

# Helper function to generate random shoot time within the specified range
def generate_shoot_time():
	return random.randint(10, 15)

# Helper function to generate random score for an arrow within the range of 0 to max score
def generate_arrow_score(max_score):
	return random.randint(0, max_score)

shooting_session = 1

insert_statement = ""

# for id, competition in enumerate(competitions):
# 	competition_date = datetime.strptime(competition['CompetitionDate'], '%Y-%m-%d')
# 	for day in range(competition['Duration']):
# 		for hour in random.sample(shoot_hour, k=2):
# 			session_date = competition_date.replace(hour=hour)
# 			for archer_id in random.sample(range(1, 501), k=25): 
# 				round_name = random.choice(list(rounds_dict[id].keys()))
# 				round_data = rounds_dict[id][round_name]
# 				max_score = round_data['MaxScoreByArrow']
# 				shoot_date = session_date
# 				insert_statement += f"INSERT INTO ShootingSession (ArcherId, CompetitionId, RoundName, SessionDate, Class, Division) VALUES ({archer_id}, {competition['Id']}, '{round_name}', '{shoot_date.strftime('%Y-%m-%d %H:%M:%S')}', '{archer[archer_id - 1]['Class']}', '{archer[archer_id - 1]['DefaultDivision']}');\n"
# 				insert_statement += f"INSERT INTO End (ShootingSessionId, Dist, ShootingRange, Arrow1, Arrow2, Arrow3, Arrow4, Arrow5, Arrow6, ShootDate) VALUES\n"
# 				end_data = []
# 				# Insert Arrows
# 				for dist_shooting_range, sub_round_data in round_data['SubRounds'].items():
# 					dist, shooting_range = dist_shooting_range
# 					target_face = sub_round_data['TargetFace']
# 					for _ in range(shooting_range):
# 						arrows = []
# 						for _ in range(6):
# 							score = generate_arrow_score(max_score)
# 							arrows.append(score)
# 							# arrows.append(f"({dist}, {shooting_range}, {shooting_session}, {score}, '{shoot_date.strftime('%Y-%m-%d %H:%M:%S')}')")
# 
# 						end_data.append(f"({shooting_session}, {dist}, {shooting_range}, {arrows[0]}, {arrows[1]}, {arrows[2]}, {arrows[3]}, {arrows[4]}, {arrows[5]}, '{shoot_date.strftime('%Y-%m-%d %H:%M:%S')}')")
# 						shoot_time = generate_shoot_time() * 6
# 						shoot_date += timedelta(minutes=shoot_time)
# 				insert_statement += ",\n".join(end_data) + ";\n"
# 				shooting_session += 1
# 
# with open('generated_sql/sessions.sql', 'w') as file:
# 	file.write(insert_statement)
# 
# print(shooting_session)

shooting_session = 601

competition_date = datetime.strptime("2024-03-10", '%Y-%m-%d')
duration = 10
for day in range(duration):
	for hour in random.sample(shoot_hour, k=2):
		session_date = competition_date.replace(hour=hour)
		for archer_id in random.sample(range(1, 11), k=10): 
			round_name = random.choice(list(rounds_dict[0].keys()))
			round_data = rounds_dict[0][round_name]
			max_score = round_data['MaxScoreByArrow']
			shoot_date = session_date
			insert_statement += f"INSERT INTO ShootingSession (ArcherId, CompetitionId, RoundName, SessionDate, Class, Division) VALUES ({archer_id}, 3, '{round_name}', '{shoot_date.strftime('%Y-%m-%d %H:%M:%S')}', '{archer[archer_id - 1]['Class']}', '{archer[archer_id - 1]['DefaultDivision']}');\n"
			insert_statement += f"INSERT INTO End (ShootingSessionId, Dist, ShootingRange, Arrow1, Arrow2, Arrow3, Arrow4, Arrow5, Arrow6, ShootDate) VALUES\n"
			end_data = []
			# Insert Arrows
			for dist_shooting_range, sub_round_data in round_data['SubRounds'].items():
				dist, shooting_range = dist_shooting_range
				target_face = sub_round_data['TargetFace']
				for _ in range(shooting_range):
					arrows = []
					for _ in range(6):
						score = generate_arrow_score(max_score)
						arrows.append(score)
						# arrows.append(f"({dist}, {shooting_range}, {shooting_session}, {score}, '{shoot_date.strftime('%Y-%m-%d %H:%M:%S')}')")

					end_data.append(f"({shooting_session}, {dist}, {shooting_range}, {arrows[0]}, {arrows[1]}, {arrows[2]}, {arrows[3]}, {arrows[4]}, {arrows[5]}, '{shoot_date.strftime('%Y-%m-%d %H:%M:%S')}')")
					shoot_time = generate_shoot_time() * 6
					shoot_date += timedelta(minutes=shoot_time)
			insert_statement += ",\n".join(end_data) + ";\n"
			shooting_session += 1

with open('generated_sql/staging_sessions.sql', 'w') as file:
	file.write(insert_statement)

print(shooting_session - 637 + 1)
