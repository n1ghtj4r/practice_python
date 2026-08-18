# rules on ranges loop:: range(start, stop, step)

for num in range(3):# loop range
    print(num)

print("\n")# loop stop

for num in range(1, 5):
    print(num)

print("\n")# loop stop and steps

for num in range(2, 11, 2):
    print(num)

print("\n")# loop negative

for num in range(40, 0, -10):
    print(num)

print("\n")# loop with list range

numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]