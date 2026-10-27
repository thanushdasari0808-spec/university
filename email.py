import re

email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")

# Email validation
if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email):
    print("Valid email")
else:
    print("Invalid email")

# Registration ID validation (example: NRI2026001)
if re.fullmatch(r"NRI[0-9]{7}", reg_id):
    print("Valid registration ID")
else:
    print("Invalid registration ID")

# Check missing components
if not email or "@" not in email or "." not in email:
    print("Email has missing components")

if not reg_id:
    print("Registration ID is missing")
