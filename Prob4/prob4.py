
def main():
    cand = set()
    for factor1 in range(999,99,-1):
        for factor2 in range(factor1,99,-1):
            productstr = str(factor1 * factor2)

            if productstr == productstr[::-1]:
                cand.add(int(productstr))

    print(max(cand))
if __name__ == "__main__":
    main()
