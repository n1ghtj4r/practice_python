def create_character(name, strength, intelligence, charisma):
    
    if not isinstance(name, str):
        return "The character name should be a string"
    
    if name == "":
        return "The character should have a name"
    
    if len(name) > 10:
        return "The character name is too long"
    
    if " " in name:
        return "The character name should not contain spaces"
    
    stats = [strength, intelligence, charisma]
    
    if not all(isinstance(stat, int) and not isinstance(stat, bool) for stat in stats):
        return "All stats should be integers"
    
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"
    
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"
    
    if sum(stats) != 7:
        return "The character should start with 7 points"
    
    def make_bar(value):
        return "●" * value + "○" * (10 - value)
    
    result = (
        f"{name}\n"
        f"STR {make_bar(strength)}\n"
        f"INT {make_bar(intelligence)}\n"
        f"CHA {make_bar(charisma)}"
    )
    
    return result

print(create_character("ver", 2, 2, 4))