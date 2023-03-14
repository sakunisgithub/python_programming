def minion_game(string):
    n = len(string)

    score_player_1 = score_player_2 = 0

    for i in range(n) :
        if string[i] in "AEIOU" :
            score_player_1 += n - i
        else :
            score_player_2 += n - i
    
    if (score_player_1 > score_player_2) :
        print(f"Kevin {score_player_1}")
    elif (score_player_1 < score_player_2) :
        print(f"Stuart {score_player_2}")
    else :
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)