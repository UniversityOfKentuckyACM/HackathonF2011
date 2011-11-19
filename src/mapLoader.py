def loadMap():#add map var
    mapName = "0_0.map"
    f = open("../data/maps/"+mapName,'r')
    mapName = f.readline().strip()
    alias = {}
    atLayer = []
    belowLayer = []
    entities = []

    line = f.readline().strip()
    line = f.readline().strip()
    while line != "[AT]":
        if line != "":
            pair = line.split(' ')
            alias[pair[0]]=pair[1]
        line = f.readline().strip()
        
            
    print alias

    y = 0
    line = f.readline().strip()
    while line != "[BELOW]":
        if line != "":
            atLayer.append([])
            for i in range(28):
                atLayer[y].append(line[i])
            line = f.readline().strip()
            y=y+1
    print atLayer
    y = 0
    line = f.readline().strip()
    while line != "[ENTITY]":
        if line != "":
            belowLayer.append([])
            for i in range(28):
                belowLayer[y].append(line[i])
            line = f.readline().strip()
            y=y+1
    print belowLayer
    y = 0
    line = f.readline().strip()
    while line != "":
        entities.append(line.split(' '))
        line = f.readline().strip()
        y=y + 1
        
    print entities
    print "end\n"

loadMap()
