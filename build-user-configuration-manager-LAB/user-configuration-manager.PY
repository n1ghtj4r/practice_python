def add_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    
    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings, key):
    key = key.lower()
    
    if key not in settings:
        return "Setting not found!"
    
    del settings[key]
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings):
    if not settings:
        return "No settings available."
    
    result = "Current User Settings:\n"
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"
    
    return result


# Test dictionary
test_settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled"
}

# 1. View current settings
print(view_settings(test_settings))
print("-" * 40)

# 2. Try to add an existing setting
print(add_setting(test_settings, ("THEME", "dark")))
print("-" * 40)

# 3. Add a new setting
print(add_setting(test_settings, ("volume", "high")))
print("-" * 40)

# 4. Update an existing setting
print(update_setting(test_settings, ("theme", "dark")))
print("-" * 40)

# 5. Try to update a non-existing setting
print(update_setting(test_settings, ("font", "arial")))
print("-" * 40)

# 6. Delete a setting
print(delete_setting(test_settings, "language"))
print("-" * 40)

# 7. Try to delete a non-existing setting
print(delete_setting(test_settings, "font"))
print("-" * 40)

# 8. View the final settings
print(view_settings(test_settings))