weight = int(input("Weight? "))
unit = input("Kgs(type -> k) or Lbs(type -> l): ")

if unit == "k":
	converted = weight / 0.45
	print("Your weight in Kgs is " + str(converted))
else:
	converted = weight * 0.45
	print("Your weight in Lbs is " + str(converted))
