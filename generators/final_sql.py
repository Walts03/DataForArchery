files = [
	"default_sql/table.sql",
	"default_sql/class.sql",
	"default_sql/distance.sql",
	"default_sql/division.sql",
	"default_sql/shootingrange.sql",
	"default_sql/round.sql",
	"default_sql/targetface.sql",
	"default_sql/subround.sql",
	"default_sql/competition.sql",
	"generated_sql/archers.sql",
	"generated_sql/sessions.sql",
]

data = ""

for file in files:
	with open(file) as fp:
		data += fp.read()
		data += "\n"

with open('archery.sql', 'w') as fp:
	fp.write(data)
