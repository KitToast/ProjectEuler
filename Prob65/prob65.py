
def main():

    #Fill list of constants
    constantList = [2]

    seqGen = genSequence()
    for _ in range(0,98): #Shift back by one to account for trivial first term
        constantList = constantList + [next(seqGen)]

    numerator, denominator = 1,1

    for leftInt in constantList[::-1]:
        numerator,denominator = denominator,numerator
        numerator = denominator * leftInt + numerator #swap

    denoTup = tuple(str(numerator))

    accum = 0
    for i in denoTup:
        accum += int(i)
    print(accum)

def genSequence():
    i = 1
    while True:
        yield 1
        yield 2 * i
        yield 1
        i += 1

if __name__ == "__main__":
    main()
