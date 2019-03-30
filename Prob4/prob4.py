
def main():

    for factor1 in range(999,99,-1):
        for factor2 in range(factor1,99,-1):
            product = str(factor1 * factor2)

            if product == product[::-1]:
                print(product)
                return


if __name__ == "__main__":
    main()
