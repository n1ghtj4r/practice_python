programming_languages = ['Rust', 'Java', 'Python', 'C++'] # loop programming language

for language in programming_languages:
    print(language)

print("\n")# loop characters

for char in 'code':
    print(char)

print("\n")# fruit category

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

print("\n") # guess number

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')

print("\n") # letters range limit

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)

print("\n") # letters range limit

developer_names_range_limit = ['Jess', 'Naomi', 'Tom']

for developer_picker in developer_names_range_limit:
    if developer_picker == 'Naomi':
        continue
    print(developer_picker)

print("\n") # letters

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")