SQFT_PER_ACRE = 43560

length = float(input("Input length: "))
width = float(input("Input width: "))

area = length * width / SQFT_PER_ACRE

print("Area is", area, "acres.")
