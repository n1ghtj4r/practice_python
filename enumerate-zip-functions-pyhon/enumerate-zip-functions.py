languages = ['Spanish', 'English', 'Russian', 'Chinese']

for language in languages:
    print(language)

print("\n")

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1

print(list(enumerate(languages)))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

print("\n")

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

print("\n")

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')

print("\n")

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

print("\n")

for name, dev_id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {dev_id}')