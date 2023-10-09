popMarrakech = 1000000
popAgadir = 500000
annees = 0

while popAgadir <= popMarrakech:
    popMarrakech += 50000
    popAgadir *= 1.08
    annees += 1

print(annees)
