

def main():
    #Note that it suffices to define two consecutive nodes and the edge nodes to determine the rest of the gon.
    fillRill(12)


#Brute force, terrible nested loop version
def fillRill(constraint):
    magicRing = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    uniqueList = []

    upperNodeConstraint = min(constraint,10)
    for upperNode in range(1,11):

        magicRing[0][0] = upperNode

        for lowerNode in range(1,11):
            magicRing[0][1] = lowerNode
            magicRing[0][2] = constraint - (upperNode + lowerNode)

            if(magicRing[0][2] > 0):

                magicRing[1][1] = magicRing[0][2]
                loweredge2 = magicRing[1][1]
                for edge2 in range(1,11):
                    magicRing[1][0] = edge2
                    magicRing[1][2] = constraint - (edge2 + loweredge2)

                    if(magicRing[1][2] > 0):

                        magicRing[2][1] = magicRing[1][2]
                        loweredge3 = magicRing[2][1]

                        for edge3 in range(1,11):
                             magicRing[2][0] = edge3
                             magicRing[2][2] = constraint - (edge3 + loweredge3)

                             if(magicRing[2][2] > 0):

                                magicRing[3][1] = magicRing[2][2]
                                loweredge4 = magicRing[3][1]

                                for edge4 in range(1,11):
                                     magicRing[3][0] = edge4
                                     magicRing[3][2] = constraint - (edge4 + loweredge4)

                                     if(magicRing[3][2] > 0):

                                        magicRing[4][1] = magicRing[3][2]
                                        loweredge5 = magicRing[4][1]

                                        for edge5 in range(1,11):
                                             magicRing[4][0] = edge5
                                             magicRing[4][2] = constraint - (edge5 + loweredge5)

                                             if(magicRing[4][2] > 0):

                                                 uniqueValSet = set(tuple(i) for i in magicRing) #Nice idiom to get unique expressions
                                                 if len(uniqueValSet) == 5:
                                                    uniqueList.append(magicRing.copy())
    filterUniqueList(uniqueList)

def filterUniqueList(list):

    def concatList(list):
        accum = ""
        for i in list:
            accum += i
        return accum



if __name__ == "__main__":
    main()
