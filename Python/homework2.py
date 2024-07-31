# Use input for the two logical values
value1 = input("Enter the first value (True or False): ").lower() == "true"
value2 = input("Enter the second value (True or False): ").lower() == "true"

# and
print("AND Result:", value1 and value2)

# or
print("OR Result:", value1 or value2)

# Not for both values
print("not (first value):", not value1)
print("not (second value):", not value2)

print("Equality comparison:", value1 == value2)

print("Inequality comparison:", value1 != value2)
