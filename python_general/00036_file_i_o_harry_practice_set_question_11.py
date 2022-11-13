import os
f = open("first_python.txt", "r")
content = f.read()
f.close()

os.remove("first_python.txt")

f = open("renamed_by_python.txt", "w")
f.write(content)
f.close()
