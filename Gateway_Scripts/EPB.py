qvName=("Emergency Generator B")
qv=system.tag.read("GenB")
on="ON"

qv=system.tag.read("changer 2")


if qv.value>=1:
	#system.db.runPrepUpdate("INSERT INTO users (Name,Age) VALUES (?,?);", [uz.value],[qv.value], 'python')
	system.db.runPrepUpdate("INSERT INTO users (Name,Overage) VALUES (?,?);", [str(qvName), qv.value], 'python')
	system.tag.write("EMB",3.0)
	
elif qv.value==0:
	system.tag.write("EMB",0.0)
