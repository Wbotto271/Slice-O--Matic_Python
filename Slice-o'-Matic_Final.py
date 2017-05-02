# http://ascii.co.uk/art/pizza and
#http://patorjk.com/software/taag/#p=display&f=Big&t=Slice%20-%20o'-%20Matic


import math
import sys

print ("                                            ___"        )
print ("                                           |  ~~--.")
print ("                                           |%=@%%/")
print ("                                           |o%%%/")
print ("                                        __ |%%o/")
print ("                                  _,--~~ | |(_/ ._")
print ("                               ,/'  m%%%%| |o/ /  `\.")
print ("                              /' m%%o(_)%| |/ /o%%m `\ ")
print ("                            /' %%@=%o%%%o|   /(_)o%%% `\ ")
print ("                           /  %o%%%%%=@%%|  /%%o%%@=%%  \ ")
print ("                          |  (_)%(_)%%o%%| /%%%=@(_)%%%  |")
print ("                          | %%o%%%%o%%%(_|/%o%%o%%%%o%%% |")
print ("                          | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |")
print ("   _____ _ _              | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |")
print ("  / ____| (_)              \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /")
print (" | (___ | |_  ___ ___       \. ~o%%(_)%%%o%(_)%%(_)o~ ,/")
print ("  \___ \| | |/ __/ _ \        \_ ~o%=@%(_)%o%%(_)%~ _/")
print ("  ____) | | | (_|  __/          `\_~~o%%%o%%%%%~~_/'")
print (" |_____/|_|_|\___\__               `--..____,,--'")
print ("                 _          __  __       _   _  ")
print ("                ( )        |  \/  |     | | (_) ")      
print ("  ______    ___ |/ ______  | \  / | __ _| |_ _")
print (" |______|  / _ \  |______| | |\/| |/ _` | __| |/ __| ")
print ("          | (_) |          | |  | | (_| | |_| | (__ ")       
print ("           \___/           |_|  |_|\__,_|\__|_|\___| ")

print ("Welcome to Slice-o'-Matic!! This program is designed to tell you everything you need to know about your pizza.")
print ("This program was conceptualized and programmed by Garrett Mahoney and Will 'The King of TCP/IP' Botto.")

def Main():
    def recycle():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        answer = input("Would you like to learn about another pizza (yes/no): ")
        
        if answer == "yes":
        
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Welcome back")
            Main()
        elif answer == "no": 
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("Goodbye, and thank you for choosing Slice -o'- Matic today!!!")
            sys.exit()
        else:
            print ("Invalid input")
            recycle()
        
    def Returnstand(arc,cir,R,area,angle,sector,D,Slice): #function that handles all output of values to the user for standard pizza
        print("All values are rounded to the second decimal place... Pizza is delicious, not complicated.")
        print ("You have a",D,"inch pizza, with a circumference of",round(cir,2),".")
        print ("This Pizza has an an area of",round(area,2),",and each of it's",Slice,"slices has an area of",round(sector,2))
        print ("The arc length of each slice is",round(arc,2))

        recycle()

    def Returnsic(areacut,area,L,W,Slice): #function that handles all output of values to the user for sicilian pizza
        print("All values are rounded to the second decimal place... Pizza is delicious, not complicated.")
        print ("You have a pizza with a length of",L,"and a width of",W,".")
        print ("This Pizza has an an area of",round(area,2),"and each of it's",Slice,"slices has an area of",round(areacut,2))
        recycle()
        
    def Mathstand (D,Slice): #function for handling all "complex" pizza calculations
        R = D/2 #converts the pizza size (Diameter) to the radius of the circle
        cir = 2*math.pi*R #calculates the circumference of the users pizza
        angle = 360/Slice #determines the internal angle of the sector, the sector is the slice of pizza
        area = math.pi*R**2 #calculates the area of the circle
        arc = cir*(angle/360) #calculates the arc length of the pizza
        sector = (angle/360)*area #calculates the area of the pizza slice
        Returnstand(R,cir,angle,area,arc,sector,D,Slice)
    
    def Mathsic (L,W,Slice): #function for handling all "complex" pizza calculations
        area = L*W #calculates the area of the rectangle
        areacut = area/Slice
        Returnsic(areacut,area,L,W,Slice)
    

    def standardSlice(D):
        try:
            Slice = int(input("Please enter the number of slices for your pizza. This number must be even: "))
        except ValueError:
           print("OOPS, I didnt get that. PLease enter a numeric value.")
           standardSlice(D)
        if (Slice % 2 == 0): #even
                if (Slice>1): #checks if the user has input a value lower than 2 for the number of slices in the pizza
                    
                    Mathstand(D,Slice)
        
                else: #if all values are above 0 and even, move on to the math function
                    print ("The number of slices in your pizza is too small to yeld a result.")
                    standardSlice(D)
        else: #odd
            print ("You have entered an odd number of slices for your pizza.")
            print ("Please enter an even number instead, it just looks better.")
            standardSlice(D)
    def standard():
        #if (Style == "Standard"):
        try:
            D = int(input("Common Pizza sizes are Small: 8 in, Medium: 10 in, and Large: 12 in. How big is your Pizza?: "))#Takes input for the size of the pizza
        except ValueError:
           print("OOPS, I didnt get that. PLease enter a numeric value.")
           standard()
        if (D>1): #checks if the user has input a value lower than 0 for the size of the pizza
            standardSlice(D)       
        else: #odd
            print ("Please enter a value greater than 1.")
            standard()
            
    def sicilianSlice(L,W):
        try:
            Slice = int(input("Please enter the number of slices for your pizza. This number must be even: "))
        except ValueError:
           print("OOPS, I didnt get that. PLease enter a numeric value.")
           sicilianSlice(L,W)
        if (Slice % 2 != 0 ):
            print ("You have entered an odd number of slices for your pizza.")
            print ("Please enter an even number instead, it just looks better.")
            sicilianSlice(L,W)
        elif (Slice<2):
            print("Please enter a value greater than 1.")
            sicilianSlice(L,W)
        else:
            Mathsic(L,W,Slice)
           
    def sicilianW(L):
        try:
            W = int(input("Rectangular pizza's have a length and width, measured in inches. What is the Width of your pizza?: "))#Takes input for the size of the pizza
        except ValueError:
           print("OOPS, I didnt get that. PLease enter a numeric value.")
           sicilianW(L)
        if (W>=1):
           sicilianSlice(L,W)
        else:
            print("Please enter a value greater than 1.")
            sicilianW(L)

    def sicilian():
        try:
            L = int(input("Rectangular pizza's have a length and width, measured in inches. What is the length of your pizza?: "))#Takes input for the size of the pizza
        except ValueError:
           print("OOPS, I didnt get that. PLease enter a numeric value.")
           sicilian()
        if (L>=1):
            sicilianW(L)
        else:
            print("Please enter a value greater than 1.")
            sicilian()
                
        
    print("Pizza is beautiful no matter the shape or size.")
    Style = input("Please enter whether you have a 'Sicilian' (rectangular) or a 'Standard' (circular) pizza: ")
    if (Style == "Standard"):
        standard()
    elif (Style == "Sicilian"):
        sicilian()
    else:
        print("Invalid input. PLease type 'Sicilian' or 'Standard' to continue.")
        Main()

        
Main()

