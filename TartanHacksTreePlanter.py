def letsPlantTrees():
    print("To save the world, we need to plant trees!")
    good = False
    while not good:
        numTrees = input("How many trees would you like to plant: ")
        
        if numTrees.isdigit():
            good = True
        else: 
            print("\n")
            print("That's not an integer! Try again!")
            
    print("We will plant " + numTrees +" trees!")
    numTrees = int(numTrees)
    
    for i in range (numTrees):
        printOneTree()
        lbsCarbonAbsorbed = numTrees * 48
    print("Your trees have absorbed " + str(lbsCarbonAbsorbed) + " pounds of carbon per year!")
    print("\n")
    
    good2 = False
    while not good2:
        yearsLater = input("For how long would you like your trees to grow: ")
        if yearsLater.isdigit():
            good2 = True
        else:
            print("That's not an integer! Try again!")
    
    futureCarbonAbsorbed = numTrees * 48 * int(yearsLater)
    print("\n")
    print("Your little trees absorbed " + str(futureCarbonAbsorbed) + " pounds of carbon from the world in " + str(yearsLater) + " years!")
    print("\t To bring your trees alive, go to teamtrees.\n\t org where $1 = one tree brought to life!")
    print("\n")
    print("Sorry, this is the best I can do with 5 weeks of 15-110 knowledge (> y <*)")

    
def printOneTree():
    line = 1
    if line == 1:
        print("  o  ")
        line = line + 1
        if line == 2:
            print(" ooo ") 
            line = line + 1
            if line == 3:
                print("ooooo")
                line = line + 1
                if line == 4:
                    print(" ooo ")
                    line = line + 1
                    if line == 5:
                        print("  |  ")
                        line = line + 1
                        if line == 6:
                            print("  |  ")
                            line = line + 1
                            if line == 7:
                                print("-----")

letsPlantTrees()

    

    

    


    








