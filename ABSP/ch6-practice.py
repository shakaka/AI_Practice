tableData = [['apple','orange','cherry','banana'],
             ['Alice','Bob','Carol','David'],
             ['dog','cat','mice','goose']]

def printTable(a):
    colWidth = []
    for i in range(len(a)):
        #colWidth[i]=[i]*len(tableData[i])
        for n in range(len(a[i])):
            colWidth.append(len(a[i][n]))
        colWidth.sort()
        print(colWidth) ###print the charactor length for each item
    d = []
    for e in range(len(a)):
        d.append(len(a[e]))
    d.sort()
    print(d)
    for c in range(d[-1]):
        for b in range(len(a)):
            print(a[b][c].rjust(colWidth[-1]+9),end = "")
        print("")
printTable(tableData)
