import math
# Signed Edit
string = input("Degrees, Minutes, Seconds: ")
array = string.split(":")
degrees = int(array[0]) + (int(array[1])/60) + (int(array[2])/3600)
radians = degrees * (math.pi/180)
# Comment Edit
print(radians)
