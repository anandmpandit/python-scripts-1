email = input("Enter Your Email: ").strip()

domain = email[email.index('@') + 1:]

print(f"Your domain is {domain}")