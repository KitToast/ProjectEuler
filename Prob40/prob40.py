def main():

    accum = 1
    for i in range(0,7):
        accum *= generateConstant(10**i)
    print(accum)
def generateConstant(index):
    modBase = 10
    currIndex = 1
    offset = 1
    currNum = 1

    while(1):

        if((currNum / modBase) == 1):
            modBase *= 10 #increment base by one digit
            offset += 1

        if(currIndex >= index):
            return int((str(currNum)[currIndex-index]))


        currNum += 1
        currIndex += offset


if __name__ == "__main__":
    main()
