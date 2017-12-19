stop = False
while stop is False:
    inputnumber = int(input("Enter an integer: "))
    if(inputnumber % 4 == 0):
        print("differnt")
        exit(1)
    if(inputnumber % 2 == 0):
        print("even")
    else:
        print("Odd")
    if(inputnumber == -1):
        exit(1)