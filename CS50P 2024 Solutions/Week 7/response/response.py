from validator_collection import checkers

email = input("Email: ")
print("Valid" if checkers.is_email(email) else "Invalid")
