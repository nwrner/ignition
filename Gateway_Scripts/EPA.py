qvName=("Emergency Generator A")
qv=system.tag.read("GenB")
on="ON"

qv=system.tag.read("changer 1")


if qv.value>=1:
	#system.db.runPrepUpdate("INSERT INTO users (Name,Age) VALUES (?,?);", [uz.value],[qv.value], 'python')
	system.db.runPrepUpdate("INSERT INTO users (Name,Overage) VALUES (?,?);", [str(qvName), qv.value], 'python')
	system.tag.write("EMA",3.0)
	
elif qv.value==0:
	system.tag.write("EMA",0.0)
