def generateName(first, last):
	try:
		int(first)
		int(last)
	except:
		#don something
		return (first + " " + last)
	else:
		raise(ValueError)
