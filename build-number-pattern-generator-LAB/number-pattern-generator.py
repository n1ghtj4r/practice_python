def number_pattern(n):
    if type(n) is not int:
        return "Argument must be an integer value."
    
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    result = ""
    for i in range(1, n + 1):
        if i == 1:
            result += str(i)
        else:
            result += " " + str(i)
    
    return result

print(number_pattern(5))