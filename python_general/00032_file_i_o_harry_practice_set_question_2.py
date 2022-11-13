f = open("history.txt", "r")
previous_high_score = f.read()
f.close()

def game():
	score = int(input("Enter your score in game() = "))
	return score

current_score = game()

f = open("history.txt", "w")

if previous_high_score == "" :
	f.write(f"{current_score}")
elif int(previous_high_score) < current_score :
	f.write(f"{current_score}")
elif int(previous_high_score) >= current_score :
	f.write(f"{previous_high_score}")

f.close()
