

def main():
    interval_end = 20
    arreg = 1
    divisors_list = []

    for elem in range(1,interval_end+1):

        test_arreg = elem
        for cand in divisors_list:

            if(test_arreg % cand == 0):
                test_arreg /= cand

        arreg *= test_arreg
        divisors_list.append(test_arreg)


    print(arreg)

if __name__ == "__main__":
    main()
