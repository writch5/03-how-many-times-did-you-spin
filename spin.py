spins = input("How many times did you spin? (Enter a negative number for counter-clockwise spins) ")

#TODO - Edit the degrees calculation here!
degrees = float(spins) * 360

print("You are facing", degrees % 360, "degrees relative to north")

# when I input 0.25, I should get "90.0 degrees relative to north"
# when I input 1, I should get "0.0 degrees relative to north" (back where I started)
# when I input -2, I should get "0.0 degrees relative to north" (again, back where I started)
# when I input 1.5, I should get "180.0 degrees relative to north"
