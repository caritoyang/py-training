# Dictionary
# Key must always be unique / Key and value could be any datatype

oDisc={"K1":"Val1", 2:"val2", "K3":32}

print(oDisc)
print(oDisc[2])

# Update value by key
oDisc["K3"]="TestingWorld"
print(oDisc["K3"])

# Add new value
oDisc["5"]="KinuSolutions"
print(oDisc)

# METHODS: keys, values, items, find length
print(oDisc.keys())
print(oDisc.values())
print(oDisc.items()) # Keys & Values
print(len(oDisc))