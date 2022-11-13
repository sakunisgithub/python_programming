f = open("random_text.txt", "r")
text = f.read()
if "cricket" in text :
	print("'cricket' is present in the .txt file")
else :
	print("'cricket' is not present in the .txt file")

if "music" in text :
	print("'music' is present in the .txt file")
else :
	print("'music' is not present in the .txt file")

f.close()
