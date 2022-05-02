# is a collection just like list, is unordered, changable and indexed can use keys as indexes

animals = {
    'reptiles': 'snakes',
    'reptiles': 'lizards',  # in case of duplicaiton of key accepts last value  
    'mamals':'lion',
    'amphibians': 'frog',
    1: 'me'
}

print(animals)
print(animals[1])
print(animals['mamals'])