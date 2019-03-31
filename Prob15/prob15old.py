
#Inefficient way of using DP. CAn srart with the top left most corner and precompute the values as we go.
def main():

    sum = traverseLattice(20,20)
    print(sum)

def traverseLattice(x,y):

    if(corner(x,y)):
        return 1
    else:
        return traverseLattice(x-1,y) + traverseLattice(x,y-1)

#Tests if coordinate is indeed a corner/edge
def corner(x,y):
    return  y <= 0 or x <= 0


if __name__ == "__main__":
    main()
