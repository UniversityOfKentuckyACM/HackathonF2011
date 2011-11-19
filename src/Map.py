class Map:
    
    mapName = "map"
    aliases = {}
    atLayer = []
    belowLayer = []
    entities = []
    
    def clean(self, contents):
        cleanContents = []
        for line in contents:
            line = line.strip()
            if line != "":
                if not line.startswith('\''):
                    cleanContents.append(line.split('\'')[0].strip())
        
        return cleanContents
    
    def __init__(self, mapName):
        for y in range(24):
            self.atLayer.append(['.'] * 28)
            self.belowLayer.append(['.'] * 28)
        
        f = open("../data/maps/" + mapName, 'r')
        
        contents = f.readlines()
        contents = self.clean(contents)
        print contents
        
        lineIndex = 0
        
        self.mapName = contents[lineIndex]
        
        lineIndex = lineIndex + 1 # the [RSC] tag
        lineIndex = lineIndex + 1 # move to first resource
        
        while contents[lineIndex] != "[AT]":
            pair = contents[lineIndex].split(' ')
            self.aliases[pair[0]]=pair[1]
            lineIndex = lineIndex + 1 # move to next pair or [AT] tag
        
        for y in range(24):
            lineIndex = lineIndex + 1
            for x in range(28):
                self.atLayer[y][x] = contents[lineIndex][x]
        
        lineIndex = lineIndex + 1 # the [BELOW] tag
        
        for y in range(24):
            lineIndex = lineIndex + 1
            for x in range(28):
                self.belowLayer[y][x] = contents[lineIndex][x]
        
        lineIndex = lineIndex + 1 # the [ENTITY] tag
        lineIndex = lineIndex + 1 # move to first entity
        
        while lineIndex < len(contents):
            self.entities.append(contents[lineIndex].split(' '))
            lineIndex = lineIndex + 1

