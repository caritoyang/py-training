# Nested Dictionary
odics = {
         'k1': {'id':21,'name':'Kinu'},
         'k2': {'id':22,'name':'Ceci'},
         'k3': {'id':23,'name':'Carl'}
         }

print(odics['k1']['id'])
print(odics['k2']['name'])

# add value to Main Dictionary
odics['k4'] = {'id':24,'name':'Jake'}
print(odics)

# add value to Internal Dictionary
odics['k3']['test'] = 'Testing'
print(odics)

# update value
odics['k4']['name'] = 'CHANGE'
print(odics)