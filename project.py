# import mathplotlib as mt
volt_a=[]
volt_b =[]
current_a = []
current_b = []
# devices = [[volt_a] , [current_a] , [volt_b] , [current_b]]
for device in range(2):
    option = ''
    y = 1
    if device == 0:
        print("Enter Device 1 data")
    if device == 1:
        print("Enter Device 2 data")
    while option != "n":
        for x in range(y):
            y= y+1
            if device == 0:
                volt_a.append(input("Enter Value of voltage: ")),
                current_a.append(input("Enter value of current: ")),
            elif device == 1:
                volt_b.append(input("Enter Value of voltage: ")) ,
                current_b.append(input("Enter value of current: ")) ,
            if y > 2:
                option = input("Do you want to add more values to the table: press y to add more and n to exit: ")
                if option == 'n':
                    break
            elif option == "y":
                y =2
                continue
        if option == 'n':
            break
volt = 0
for x in range(y-1):
    if (y-2) == volt:
        break
    if float(volt_a[volt+1])/float(volt_a[volt]) == float(current_a[volt+1])/float(current_a[volt]):
        passes = 1
    else:
        passes = 0,
        break
    volt+=1
if passes == 1:
    print("Device A follow ohms law")
elif passes == 0:
    print("Device A donot follow ohm law")

# Check for device 2
passes_b = 0
for x in range(y-1):
    if (y-2) == volt:
        break
    if float(volt_b[volt+1])/float(volt_b[volt]) == float(current_b[volt+1])/float(current_b[volt]):
        passes_b = 1
    else:
        passes_b = 0
        break
    volt+=1
if passes_b == 1:
    print("Device B follow ohms law")
elif passes_b == 0:
    print("Device B donot follow ohm law")
