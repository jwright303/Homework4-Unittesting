def averageList(uList):

	if(type(uList) != type([1, 3])):
		raise(ValueError)
		return

	else:
		listSum = 0
		average = 0
		if(len(uList) == 0):
			raise(ValueError)
			return
		else:
			for i in range(0, len(uList)):
				listSum = listSum + uList[i]

		average = listSum / len(uList)
		return average

