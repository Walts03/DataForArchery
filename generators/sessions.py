from datetime import datetime, timedelta
import json

rounds_dict = {
	 'WA900': {
		  'EquivalentRound': None,
		  'MaxScoreByArrow': 10,
		  'SubRounds': {
				(60, 5): {'TargetFace': 122, 'ShootingRange': 5},
				(50, 5): {'TargetFace': 122, 'ShootingRange': 5},
				(40, 5): {'TargetFace': 122, 'ShootingRange': 5}
		  }
	 },
	 'WA70': {
		  'EquivalentRound': None,
		  'MaxScoreByArrow': 10,
		  'SubRounds': {
				(70, 12): {'TargetFace': 122, 'ShootingRange': 12}
		  }
	 },
	 'WA18': {
		  'EquivalentRound': None,
		  'MaxScoreByArrow': 10,
		  'SubRounds': {
				(18, 10): {'TargetFace': 40, 'ShootingRange': 10}
		  }
	 },
	 'Metric II': {
		  'EquivalentRound': None,
		  'MaxScoreByArrow': 10,
		  'SubRounds': {
				(60, 6): {'TargetFace': 122, 'ShootingRange': 6},
				(50, 6): {'TargetFace': 122, 'ShootingRange': 6},
				(40, 6): {'TargetFace': 80, 'ShootingRange': 6},
				(30, 6): {'TargetFace': 80, 'ShootingRange': 6}
		  }
	 }
}

# Dictionary for competitions
competitions = [
	{'Id': 1, 'IsChampionship': True, 'Name': 'World Archery Championship', 'CompetitionDate': '2024-04-15', 'Duration': 7},
	{'Id': 2, 'IsChampionship': False, 'Name': 'Metric', 'CompetitionDate': '2024-06-20', 'Duration': 5}
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

archer = archers

import random

# Helper function to generate random shoot time within the specified range
def generate_shoot_time():
	return random.randint(10, 15)

# Helper function to generate random score for an arrow within the range of 0 to max score
def generate_arrow_score(max_score):
	return random.randint(0, max_score)

shooting_session = 1

insert_statement = ""

for competition in competitions:
	competition_date = datetime.strptime(competition['CompetitionDate'], '%Y-%m-%d')
	for day in range(competition['Duration']):
		for hour in shoot_hour:
			session_date = competition_date.replace(hour=hour)
			for archer_id in range(1, 5): 
				round_name = random.choice(list(rounds_dict.keys()))
				round_insert_statement = rounds_dict[round_name]
				max_score = round_insert_statement['MaxScoreByArrow']
				shoot_date = session_date
				insert_statement += f"INSERT INTO ShootingSession (ArcherId, CompetitionId, RoundName, SessionDate, Class, Division) VALUES ({archer_id}, {competition['Id']}, '{round_name}', '{shoot_date.strftime('%Y-%m-%d %H:%M:%S')}', '{archer[archer_id - 1]['Class']}', '{archer[archer_id - 1]['DefaultDivision']}');\n"
				insert_statement += f"INSERT INTO Arrow (Dist, ShootingRange, ShootingSessionId, Score, ShootDate) VALUES\n"
				arrows = []
				# Insert Arrows
				for dist_shooting_range, sub_round_insert_statement in round_insert_statement['SubRounds'].items():
					dist, shooting_range = dist_shooting_range
					target_face = sub_round_insert_statement['TargetFace']
					for _ in range(shooting_range):
						for _ in range(6):
							score = generate_arrow_score(max_score)
							arrows.append(f"({dist}, {shooting_range}, {shooting_session}, {score}, '{shoot_date.strftime('%Y-%m-%d %H:%M:%S')}')")

							shoot_time = generate_shoot_time()
							shoot_date += timedelta(minutes=shoot_time)
				insert_statement += ",\n".join(arrows) + ";\n"
				shooting_session += 1

with open('generated_sql/sessions.sql', 'w') as file:
	file.write(insert_statement)
