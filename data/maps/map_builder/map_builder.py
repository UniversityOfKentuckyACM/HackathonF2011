import os

bottomLayer = list()
sVal = 0
while (sVal < 24):
	tLay = list()
	tVal = 0
	while (tVal < 28):
		tLay.append('.')
		tVal = tVal + 1
	bottomLayer.append(tLay)
	sVal = sVal + 1

def printBottom(printType, char, x1=0, y1=0, x2=0, y2=0):
	fill = False
	if printType == 'all':
		fill = True
		x1 = 0
		x2 = 28
		y1 = 0
		y2 = 24
	elif printType == 'box':
		fill = False
	elif printType == 'fbox':
		fill = True
	y = y1
	while(y < y2):
		if (fill or (y == y1) or (y == y2-1)):
			x = x1
			while(x < x2):
				bottomLayer[y][x] = char
				x = x + 1
		else:
			bottomLayer[y][x1] = char
			bottomLayer[y][x2-1] = char
		y = y + 1
	printLayer(bottomLayer, '[UNDER]')
	return

def printLayer(layer, layerName='[]'):
	print layerName
	for each in layer:
		line = ""
		for eachChr in each:
			line = line + eachChr
		print line

def main(planName):
	planFile = open(planName, 'rb')
	lines = planFile.readlines()
	bottomMode = False
	for line in lines:
		print line
		if (line !='#B\n'):
			if (bottomMode):
				words = line.split()
				if words.index(';;') < 6:
					printBottom(words[0], words[1])
				else:
					printBottom(words[0], words[1], 0, 0, 10, 10)
		else:
			if (line == '#B\n'):
				print 'Bottom Mode'
				bottomMode = True
	return

main('sample.map.plan')
