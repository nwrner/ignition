qv=system.tag.read("Power")
uz=system.tag.read("Name")


if qv.value>=90:
	#system.db.runPrepUpdate("INSERT INTO users (Name,Age) VALUES (?,?);", [uz.value],[qv.value], 'python')
	system.db.runPrepUpdate("INSERT INTO users (Name,Overage) VALUES (?,?);", [uz.value, qv.value], 'python')
	#system.db.runPrepUpdate("INSERT INTO users (Name) VALUES (?);", [uz], 'python')


	
	
	
	
	
	
