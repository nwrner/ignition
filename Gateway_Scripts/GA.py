qvName=system.tag.read("GenA.Name")
qv=system.tag.read("GenA")


if qv.value>=100:
	#system.db.runPrepUpdate("INSERT INTO users (Name,Age) VALUES (?,?);", [uz.value],[qv.value], 'python')
	system.db.runPrepUpdate("INSERT INTO users (Name,Overage) VALUES (?,?);", [str(qvName), qv.value], 'python')
	#system.db.runPrepUpdate("INSERT INTO users (Name) VALUES (?);", [uz], 'python')

