def LCS(X,Y):
    memTable = [[0 for j in range(len(Y)+1)] for i in range(len(X) +1)]
    # row 0 and colun 0 are initialized to 0 already
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            if x == y:
                memTable[i+1][j+1] = memTable[i][j] + 1
            else:
                memTable[i+1][j+1] = max(memTable[i+1][j],memTable[i][j+1])

    #read the substring from table
    result = ""
    x,y = len(X),len(Y)

    while x !=0 and y !=0:
        if memTable[x][y] == memTable[x-1][y]:
            x-=1
        elif memTable[x][y] == memTable[x][y-1]:
            y-=1
        else:
            assert X[x-1] == Y[y-1]
            result = X[x-1] + result

            x-=1
            y-=1
    return result


if __name__ == '__main__':
    print(LCS("thisistest","testingLCS123testing"))


