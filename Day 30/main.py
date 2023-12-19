height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Huma height should not be over 3m.")

bmi = weight / height * 2
print(bmi)