presidents_usa = ["George Washington", "John Adams","Thomas Jefferson","James Madison","James Monroe","John Adams","Andrew Jackson"]
split_names = [name.split(' ') for name in presidents_usa]
print(split_names)
swapped_names = [" ".join(item[::-1]) for item in split_names]
print(swapped_names)
swapped_list = [split_name[1] + " " + split_name[0] for split_name in split_names]
print(swapped_list)

# Creating Pythagorean triplets
triplets = [(a,b,c) for a in range(1,30) for b in range(1,30) for c in range(1,30)if a**2 + b**2 == c**2]
print(triplets)

# Tuples
height_in_cms = [('Tom',183),('Daisy',171),('Margaret',179),('Michael',190),('Nick',170)]
height_in_feet = [(height[0],round(height[1]*0.0328,1)) for height in height_in_cms]
print(height_in_feet)

matrix = [[j * j+i for j in range(3)] for i in range(3)]
print(matrix)

# Set
names = [ 'Arnold', 'BILL', 'alice', 'arnold', 'MARY', 'J', 'BIll' ,'maRy']
uniq = {name.capitalize() for name in names if len(name) > 1}
print(uniq)