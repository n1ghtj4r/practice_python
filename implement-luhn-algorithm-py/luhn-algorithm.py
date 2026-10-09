def verify_card_number(card_number):
    clean_number = card_number.replace(' ', '').replace('-', '')
    
    digits = [int(digit) for digit in clean_number]
    
    total_sum = 0
    for idx, digit in enumerate(reversed(digits)):
        if idx % 2 == 1: 
            doubled = digit * 2
            total_sum += doubled - 9 if doubled > 9 else doubled
        else:
            total_sum += digit
            
    if total_sum % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'

# output
print(verify_card_number('453914889'))             # VALID
print(verify_card_number('4111-1111-1111-1111'))   # VALID
print(verify_card_number('1234 5678 9012 3456'))   # INVALID