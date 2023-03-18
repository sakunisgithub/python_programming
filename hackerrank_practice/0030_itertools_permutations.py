from itertools import permutations

given_input = input().split()

given_input[1] = int(given_input[1])

letters = [a for a in given_input[0]]

output_list = list(permutations(letters, given_input[1]))

final_permutations = []

for i in range(len(output_list)) :

    temp = ""

    for j in range(given_input[1]) :

        temp = temp + output_list[i][j]

    final_permutations.append(temp)

final_permutations.sort()

for i in range(len(final_permutations)) :
    print(final_permutations[i])