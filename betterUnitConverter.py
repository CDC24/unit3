#Caleb Callaway
#2/26/18
#betterUnitConverter.py - uses if statements and loops to allow user to choose a conversion type and perform it

print ("Which conversion would you like to perform?  1) Kilometers to meters,  2) Kilograms to pounds,  3) Liters to gallons,  4) Celsius to Fahrenheit, or 5) quit the program")

while True:
    conversion = int(input("Enter the number of the conversion you would like to perform. "))
    
    if conversion == 5:
        break
    elif conversion == 1:
        km = float(input("Enter a number of kilometers: "))
        print (km,"Km =",km*0.621371192,"miles.")
    elif conversion == 2:
        kg = float(input("Enter a number of kilograms: "))
        print (kg,"Kg =",kg*2.20462,"pounds.")
    elif conversion == 3:
        L = float(input("Enter a number of liters: "))
        print (L,"Liters =",L*0.264172,"gallons.")
    elif conversion == 4:
        C = float(input("Enter a number of degrees Celcius: "))
        print (C,"Degrees Celsius =",(C*1.8)+32,"Degrees Fahrenheit.")
    
    else:
        print ("Uh, think again, dummy. Numbers 1-5, please...?")
        break
