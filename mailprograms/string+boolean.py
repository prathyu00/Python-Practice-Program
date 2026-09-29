password = "admin123"
is_strong = len(password) >= 8 and any(ch.isdigit() for ch in password)
print("Password:", password)
print("Is strong?", is_strong)