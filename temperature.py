temp = float(input("What's the temp? "))
scale = input("Fahrenheit(F) or Celius(C)?: ").lower()

if scale == "f":
	cel = (temp - 32) * 5/9
	print(cel)
elif scale == "c":
	fah = (temp * 1.8) + 32
	print(fah)
else: 
	print("Wrong scale!")


