def main():

    largestLen = 0;
    largestStarting = 0;

    for startingnum in range(1,1000001):
        
        len = computeSequence(startingnum)

        if(len > largestLen):
            largestStarting = startingnum
            largestLen = len

    print(largestStarting)


def computeSequence(startingnum):
    length = 0
    currnum = startingnum

    while(currnum > 1):
        length += 1
        if((currnum % 2) == 0):
            currnum = currnum / 2
        else:
            currnum = 3*currnum + 1

    return length

if __name__ == "__main__":
    main()
