
def main():

    places = 1
    prev = 0
    curr = 1
    index = 1

    while(places < 6):

        if (curr // 100 > 0):
            result = curr + prev
            prev = curr // 10
            curr = result // 10
        else:
            result = curr + prev
            prev = curr
            curr = result
        index += 1
    print(index)




if __name__ == "__main__":
    main()
