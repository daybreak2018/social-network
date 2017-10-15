import re
with open("./bootcamp/urls.py", "r") as sources:
    lines = sources.readlines()
with open("./bootcamp/urls.py", "w") as sources:
    for line in lines:
        sources.write(re.sub(r'signup_for_hostel', 'ola', line))