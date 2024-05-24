import gpudb

import argparse
import getpass

parser = argparse.ArgumentParser(description='Import data into kinetica.')
parser.add_argument(
	'username',
	type=str,
)

args = parser.parse_args()

kinetica_password = getpass.getpass("Enter your Kinetica password: ")

options = gpudb.GPUdb.Options()
options.username = args.username
options.password = kinetica_password

kdb = gpudb.GPUdb(
  host=["https://cluster1450.saas.kinetica.com/cluster1450/gpudb-0"],
  options = options
)

def create_table(name, cols):
	global kbd

	return gpudb.GPUdbTable(
		_type = cols,
		name = name,
		db = kdb,
	)


# with open("./archery.sql", "r") as f:
# 	h_db.execute_sql(f.read())
# 
# with open("./generated_sql/archers.sql", "r") as f:
# 	h_db.execute_sql(f.read())
# 
# with open("./generated_sql/sessions.sql", "r") as f:
# 	h_db.execute_sql(f.read())
# 
# list_tables_response = h_db.show_table("Archer")
# print("Tables in Kinetica:")
# print(list_tables_response)

# Define schema
schema = "archery_competition"
kdb.create_schema(schema)

# Define table names with the schema in Capitalized Camel Case
tables = {
	"End": f"{schema}.end",
	"ShootingSession": f"{schema}.shooting_session",
	"Archer": f"{schema}.archer",
	"Competition": f"{schema}.competition",
	"SubRound": f"{schema}.sub_round",
	"TargetFace": f"{schema}.target_face",
	"Distance": f"{schema}.distance",
	"Division": f"{schema}.division",
	"Class": f"{schema}.class",
	"ShootingRange": f"{schema}.shooting_range",
	"Round": f"{schema}.round"
}

table_objs = {}

# Drop tables if they exist
for table in tables.values():
	kdb.clear_table(table, options={"no_error_if_not_exists": "true"})

# Create tables
archer_columns = [
	["Id", "int", "auto_increment", "primary_key"],
	["Name", "string", "char255"],
	["DOB", "datetime"],
	["Gender", "string", "char255"],
	["DefaultDivision", "string", "char255"]
]
table_objs["Archer"] = create_table(tables["Archer"], archer_columns)

target_face_columns = [
	["Size", "int", "primary_key"]
]
table_objs["TargetFace"] = create_table(tables["TargetFace"], target_face_columns)

distance_columns = [
	["Dist", "int", "primary_key"]
]
table_objs["Distance"] = create_table(tables["Distance"], distance_columns)

shooting_range_columns = [
	["EndNo", "int", "primary_key"]
]
table_objs["ShootingRange"] = create_table(tables["ShootingRange"], shooting_range_columns)

division_columns = [
	["Name", "string", "char255", "not_nullable"],
	["ACR", "string", "char255", "primary_key"]
]
table_objs["Division"] = create_table(tables["Division"], division_columns)

class_columns = [
	["Name", "string", "char255", "primary_key"]
]
table_objs["Class"] = create_table(tables["Class"], class_columns)

round_columns = [
	["Name", "string", "char255", "primary_key"],
	["Equivalent", "string", "char255", "nullable"],
	["MaxScoreByArrow", "int"]
]
table_objs["Round"] = create_table(tables["Round"], round_columns)

sub_round_columns = [
	["Dist", "int"],
	["ShootingRange", "int"],
	["TargetFace", "int"],
	["RoundName", "string", "char255"],
	["primary_key", ["Dist", "ShootingRange", "TargetFace", "RoundName"]],
	["FOREIGN_KEY_TargetFace", "int", "references", tables["TargetFace"], "Size"],
	["FOREIGN_KEY_Dist", "int", "references", tables["Distance"], "Dist"],
	["FOREIGN_KEY_ShootingRange", "int", "references", tables["ShootingRange"], "EndNo"],
	["FOREIGN_KEY_RoundName", "string", "char255", "references", tables["Round"], "Name"]
]
table_objs["SubRound"] = create_table(tables["SubRound"], sub_round_columns)

competition_columns = [
	["Id", "int", "auto_increment", "primary_key"],
	["IsChampionship", "boolean"],
	["Name", "string", "char255", "unique"],
	["Duration", "int"],
	["CompetitionDate", "timestamp", "default_current_timestamp"]
]
table_objs["Competition"] = create_table(tables["Competition"], competition_columns)

shooting_session_columns = [
	["Id", "int", "auto_increment", "primary_key"],
	["ArcherId", "int"],
	["CompetitionId", "int"],
	["RoundName", "string", "char255"],
	["Division", "string", "char255"],
	["Class", "string", "char255"],
	["SessionDate", "timestamp", "default_current_timestamp"],
	["FOREIGN_KEY_ArcherId", "int", "references", tables["Archer"], "Id"],
	["FOREIGN_KEY_CompetitionId", "int", "references", tables["Competition"], "Id"],
	["FOREIGN_KEY_Division", "string", "char255", "references", tables["Division"], "ACR"],
	["FOREIGN_KEY_RoundName", "string", "char255", "references", tables["Round"], "Name"]
]
table_objs["ShootingSession"] = create_table(tables["ShootingSession"], shooting_session_columns)

end_columns = [
	["Id", "int", "auto_increment", "primary_key"],
	["ShootingSessionId", "int"],
	["Dist", "int"],
	["ShootingRange", "int"],
	["Arrow1", "int"],
	["Arrow2", "int"],
	["Arrow3", "int"],
	["Arrow4", "int"],
	["Arrow5", "int"],
	["Arrow6", "int"],
	["ShootDate", "timestamp", "default_current_timestamp"],
	["FOREIGN_KEY_Dist", "int", "references", tables["Distance"], "Dist"],
	["FOREIGN_KEY_ShootingRange", "int", "references", tables["ShootingRange"], "EndNo"],
	["FOREIGN_KEY_ShootingSessionId", "int", "references", tables["ShootingSession"], "Id"]
]
table_objs["End"] = create_table(tables["End"], end_columns)

print("All tables created successfully.")

for key in tables.keys():
	with open(f"./{key}.json") as f:
		data = json.load(f)
		table_objs[key].insert_records(data)
		print(f"Inserted Data for {key}")	
