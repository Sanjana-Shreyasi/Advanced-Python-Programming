#Practice Unit : 3
fname = "notes.txt"

with open(fname, "w") as f:
    f.write("Python is easy to learn.\n")
    f.write("File handling helps to store data permanently.\n")
    f.write("We can read write and append data in files.")

print("Data saved in file")

with open(fname, "r") as f:
    content = f.read()

print("File content is")
print(content)

total_lines = content.splitlines()
total_words = content.split()
total_chars = len(content)

print("Lines:", len(total_lines))
print("Words:", len(total_words))
print("Characters:", total_chars)

with open(fname, "a") as f:
    f.write("\nThis line got added later.")

print("Line added at end")

with open(fname, "r") as f:
    updated_content = f.read()

print("File content now is")
print(updated_content)

search_word = input("Enter word to search: ")

if search_word.lower() in updated_content.lower():
    print("Word found")
else:
    print("Word not found")

#Output
'''Data saved in file
File content is
Python is easy to learn.
File handling helps to store data permanently.
We can read write and append data in files.
Lines: 3
Words: 21
Characters: 115
Line added at end
File content now is
Python is easy to learn.
File handling helps to store data permanently.
We can read write and append data in files.
This line got added later.
Enter word to search: python
Word found'''