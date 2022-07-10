print("Hey! This is a unit convertor made using python")


# Length Convertor
length_values = ["Meter(m)", "Kilometer(km)", "Centimeter(cm)", "Milliimeter(mm)"]

print("Currently you are using length convertor")
print("The values which you are allowed to use are:")

for i in range(0,4):
    print(length_values[i])

from_choice = str(input("From which unit you want to convert (use abbreviations given in brackets) :"))
to_choice = str(input("To which unit you want to convert (use abbreviations given in brackets) :"))
length_value = float(input("Enter the value:"))


if from_choice == "cm" and to_choice == "m":
    ans = float(length_value)/100  
    print(f"{ans} m")     
elif from_choice == "mm" and to_choice == "cm":
    ans = float(length_value)/10
    print(f"{ans} cm")     
elif from_choice == "m" and to_choice== "cm":
    ans = float(length_value)*100
    print(f"{ans} cm")     
elif from_choice == "cm" and to_choice == "mm":
    ans = float(length_value)*10
    print(f"{ans} mm")     
elif from_choice == "mm" and to_choice == "m":
    ans = float(length_value)/1000
    print(f"{ans} m")    
elif from_choice == "m" and to_choice== "mm":
    ans = float(length_value)*1000  
    print(f"{ans} mm")     
elif from_choice == "km" and to_choice == "m":
    ans = float(length_value)*1000
    print(f"{ans} m")     
elif from_choice == "m" and to_choice== "km":
    ans = float(length_value)/1000
    print(f"{ans} km")     
elif from_choice == "mm" and to_choice == "km":
    ans = float(length_value)/1000000
    print(f"{ans} km")
