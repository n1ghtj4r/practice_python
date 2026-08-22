#dictionary = {
 #   key1: value1,
 #  key2: value2
#}

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

#dictionary[key] method to access the value

print(pizza['name'])

# dictionary

pizza_line = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

print(pizza_line['name'])

pizza['name'] = 'Margherita'

print(pizza['name']) # 'Margherita'

#dictionary.get(key, default)  //The .get() method retrieves the value associated with a key.

print(pizza.get('toppings', [])) # ['mozzarella', 'basil']

print(pizza.keys())
# dict_keys(['name', 'price', 'calories_per_slice'])

print(pizza.values())
# dict_values(['Margherita Pizza', 8.9, 250])

print(pizza.items())
# dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])

print(pizza.clear()) # The .pop() method removes the key-value pair with the key that you specify as the first argument and returns its value.

print(pizza.pop('price', 10))
#pizza.pop('total_price') # KeyError

#pizza.popitem()

pizza_line.update({ 'price': 15, 'total_time': 25 })

print(pizza_line)