
def main():

#Fill Triangle List
    triangle = [[0] * n for n in range(1,16)]

    file = open("data.txt")

    str = file.read()
    splitArray = str.split(" ")

    index = 0

    for i in range(0,15):
        for j in range(0,i+1):
            triangle[i][j] = int(splitArray[index])
            index += 1
# Use DP to find optimal path.

    triangleTable = [[0] * n for n in range(1,16)]
    triangleTable[0][0] = 75

    for i in range(1,15):
        for j in range(0,i+1):
            if j == 0: #Edge cases
                triangleTable[i][j] = triangle[i][j] + triangleTable[i-1][j]
            elif j == i:
                triangleTable[i][j] = triangle[i][j] + triangleTable[i-1][j-1]
            else:
                triangleTable[i][j] = max(triangle[i][j] +  triangleTable[i-1][j-1],triangle[i][j] +  triangleTable[i-1][j])

    print(max(triangleTable[14]))

if __name__ == "__main__":
    main()
