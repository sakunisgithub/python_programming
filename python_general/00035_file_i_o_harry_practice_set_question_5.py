f = open("text_file_2.txt", "r")
text = f.read()
f.close()

restricted_words = ["cricket", "bats", "sledge", "money", "balls"]

for item in restricted_words :
	if item in text :
		text = text.replace(item, "######")

f = open("text_file_2.txt", "w")
f.write(text)
f.close()
