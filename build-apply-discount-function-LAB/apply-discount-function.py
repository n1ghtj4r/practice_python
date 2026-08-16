def apply_discount(price, discount):
    if type(price) not in (int, float):
        return "The price should be a number"
    
    if type(discount) not in (int, float):
        return "The discount should be a number"
    
    if price <= 0:
        return "The price should be greater than 0"
    
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    return price * (1 - discount / 100)

print(apply_discount(100, 10));