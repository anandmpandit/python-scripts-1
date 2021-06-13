print("This is your Email Domain Name finder Python Program ")
print("Created by Gaurav Pandey")

email = input("Enter Your Email: ").strip()

domain = email[email.index('@') + 1:]

print(f"Your domain is {domain}")