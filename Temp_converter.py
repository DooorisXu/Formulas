print("Are you putting in Celsius or Farenheit?")
unit = (input('')).lower()
print("Enter the temperature in your chosen unit:")
temp = int(input(""))

print(unit)
if unit == "celsius":
    new = "%.2f" %(temp*9.0/5.0+32)
    print('The temperature in Farenheit is: ',new)
elif unit == "farenheit":
    new = "%.2f" %((temp-32)*5.0/9.0)
    print('The temperature in Celsius is: ', new)
else:
    print('Invalid input.')



