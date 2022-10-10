""" This program
is calculating Area
Written by Ana
"""
print "Calculator is starting"
name = raw_input("What's your name? ")
option = raw_input("Enter C for Circle or T for Triangle: ")

if option == 'C':
  radius = float(raw_input("Enter radius of your circle: "))
  area = 3.14159 * (radius ** 2)
  print "Area: %s" % (area)
elif option == "T":
    base = float(raw_input("Enter base of your triangle: "))
    height = float(raw_input("Enter height of your triangle: "))
    area = 0.5 * base * height
    print "Area: %s" % (area)
else:
  print "Error"


print "Exit"
