#Lazy evaluation of Triangle numbers
#Function to generate word values

import itertools
import string

def main():

    wordDic = dict(zip(list(string.ascii_uppercase), range(1,27)))

    file = open("p042_words.txt")
    fileStr = (file.read()).split(",")

    setofTriNums = 0 #Number of triangle words in file
    generatedIndex = 0 #Index of highest generated triangle number

    for index in range(0,len(fileStr)):
        str = fileStr[index][1:len(fileStr[index])-1]

        wordValue = 0
        for i in list(str):
            wordValue += wordDic[i]

        if(triangleNumGen(wordValue)):
            setofTriNums += 1

    print(setofTriNums)

def triangleNumGen(num):
    i = 1
    curr = 0

    while num >= curr:
        if(num == curr):
            return True
        curr = (i*(i+1)) / 2
        i += 1
    return False

if __name__ == "__main__":
    main()
