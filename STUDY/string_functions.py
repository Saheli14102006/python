name='saheli'
print(len(name))
print(name.endswith('aheli'))
print(name.endswith('I'))
print(name.startswith('Sa'))
print('HELLO'.lower())
print(name.capitalize())
print(name.find('h'))
print(name.replace('h','e'))
letter= ''' Dear <|Name|>,
           You are selected!
           <|Date|> '''
print(letter.replace('<|Name|>','Saheli Mondal').replace('<|Date|>','30.11.2025'))