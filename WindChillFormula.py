t = float(input("Enter the temperature:"))
v = float(input("Enter the velocity of the wind:"))
'''
print(t)
print(v)
'''
WindChill = float(35.74 + 0.6215*t + v**0.16*(0.4275*t-35.75))
print(WindChill)
print("%.2f" % WindChill)
