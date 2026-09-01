#Assignment : 8
f1 = open("input.txt", "w")
f1.write("this is line one\n")
f1.write("this is line two\n")
f1.write("this is line three\n")
f1.write("this is line four\n")
f1.close()

f1 = open("input.txt", "r")
all_lines = f1.readlines()
f1.close()

print("Total lines in file:", len(all_lines))

first_two = all_lines[0:2]

f2 = open("output.txt", "w")
f2.writelines(first_two)
f2.close()

print("First two lines written to new file")

f2 = open("output.txt", "r")
data = f2.read()
f2.close()

print("Content of output file is")
print(data)

#Output
'''Total lines in file: 4
First two lines written to new file
Content of output file is
this is line one
this is line two'''