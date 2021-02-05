def calcCubeVol(height, width, length):
	try:
		#First check to see if its a number
		#Multiplies by 1000 to see if its a decimal
		newH = int(height * 100000)
		newW = int(width * 100000)
		newL = int(length * 100000)
	except:
		raise(ValueError)

	else:
		#Divides by 1000.0 to get the origional input 
		newH = newH / 100000.0
		newW = newW / 100000.0
		newL = newL / 100000.0
		#If input not divisible by 1 then its a decimal so return error
		#Also has to be a positive year
		if newH > 0 and newW > 0 and newL > 0:
			return (newH * newW * newL)
		else:
			raise(ValueError)

