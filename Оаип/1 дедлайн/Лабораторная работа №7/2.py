password = input()
confirm = input()
if password == confirm:
    login_attempt = input()
    print("Access" if login_attempt == password else "Denied")
else:
    print("Error: passwords do not match")