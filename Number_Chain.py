repeat_ = "y"
counter = 0
while repeat_ == "y":

    #counter = 0 #to reset

    #get input
    print("How many numbers? ")

    letsgo = 0
    letsgo = int( input () )

    print("Counting up!")

    #give output
    while letsgo > 0:
        print(counter)
        counter = counter + 1
        letsgo = letsgo - 1

    print("Let's go again?")

repeat_ = input()[0]