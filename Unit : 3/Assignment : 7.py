#Assignment : 7
import re

msg = input("Enter some text: ")

pattern = r'[a-zA-Z0-9._%+]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}'

found = re.findall(pattern, msg)

if found:
    print("Emails found in text")
    for e in found:
        print(e)
else:
    print("No email present in text")

#Output
'''Enter some text: you can reach me at rahul123@gmail.com or priya.k@college.edu for details
Emails found in text
rahul123@gmail.com
priya.k@college.edu'''