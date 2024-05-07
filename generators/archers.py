import faker
from faker import Faker
import json

fake = Faker()

num_entries = 10

# Possible divisions and genders
divisions = ['R', 'C', 'B', 'L']
genders = ['Male', 'Female']

# Generate fake archers
archers = []
for _ in range(num_entries):
	archer = {
		'Name': fake.name(),
		'DOB': str(fake.date_of_birth(minimum_age=18, maximum_age=60)),
		'Gender': fake.random.choice(genders),
		'DefaultDivision': fake.random.choice(divisions)
	}
	archers.append(archer)

# Write a batched SQL insert statement
insert_statement = "INSERT INTO Archer (Name, DOB, Gender, DefaultDivision) VALUES "
values_list = []

for archer in archers:
	archer_name = archer['Name'].replace("'", "''")
	values = f"('{archer_name}', '{archer['DOB']}', '{archer['Gender']}', '{archer['DefaultDivision']}')"
	values_list.append(values)

# Combine all values in a single insert statement
insert_statement += ",\n".join(values_list) + ";"

with open('generated_sql/archers.sql', 'w') as file:
	file.write(insert_statement)

# Export archers to a JSON file for future use in another Python script
with open('generated_data/archers_data.json', 'w') as json_file:
	json.dump(archers, json_file)

