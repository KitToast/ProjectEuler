


def main():

    arreg = 3 * ((333*334)/2)

    for i in range(5,1000,5):
        arreg += (0 if (i % 3 == 0) else i)

    print(arreg)

if __name__ == "__main__":
    main()
