from sys import argv
users=[]
r = open("username_held_by_others.lst",'r').readlines()
for _ in r:
	users.append(_.strip())


try:
	if int(argv[2]):
		if argv[1] in users:
			pass
		else:
			print("Done",argv[1])
			f = open("username_held_by_others.lst",'w')
			for _ in users:
				f.write(_+"\n")
			f.write(argv[1]+"\n")
			f.close()
	else:
		if argv[1] in users:
			f = open("username_held_by_others.lst",'w')
			users.remove(argv[1])
			for _ in users:
				f.write(_+"\n")
			f.close()

except Exception as e:
	print(str(e))