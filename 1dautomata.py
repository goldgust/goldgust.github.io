
def returnstate(rule, neighbours):
    # rule = int neighbours = string
    return format(rule, 'b').zfill(8)[7 - int(neighbours, 2)]

def nextrow(rule, row):
    #rule = int row = string
    newrow = ''
    for i in range(len(row)):
        neighbours = row[(i - 1) % len(row)] + row[(i) % len(row)] + row[(i + 1) % len(row)]
        newrow += returnstate(rule, neighbours)
    return newrow

#print(returnstate(7, '111'))
def printrows(rule, row, length):
    for i in range(length):
        print(row.replace("0", " ").replace("1", "█"))
        row = nextrow(rule, row)

printrows(30, '0000110000000000000010000000000000000000000000000000000000', 30)
