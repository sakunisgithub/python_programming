f = open("text_file.txt", "r")
text = f.read()
if "donkey" in text :
	text = text.replace("donkey", "#####")
f.close()

f = open("text_file.txt", "w")
f.write(text)
f.close()
