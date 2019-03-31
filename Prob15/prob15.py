
def main():

    sum = traverseLattice(20,20)
    print(sum)

def traverseLattice(x,y):

    memo = [ [0] * (y+1) ] * (x+1)

    for y in range(0,y+1):
        memo[y][0] = 1


    for x in range(0,x+1):
        memo[0][x] = 1


    x0 = 1 #Start with lefmost corner
    y0 = 1

    while(y0 < (y+1)):
        x0 = 1
        while(x0 < (x+1)):
            memo[y0][x0] = memo[y0-1][x0] + memo[y0][x0-1]
            x0 += 1
        y0 += 1


    return memo[y][x]


if __name__ == "__main__":
    main()
