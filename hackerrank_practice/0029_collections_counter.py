from collections import Counter

number_of_shoes = int(input())

shoe_sizes = input().split()

for i in range(len(shoe_sizes)) :
    shoe_sizes[i] = int(shoe_sizes[i])

shoe_dictionary = Counter(shoe_sizes)

number_of_customers = int(input())

demands = []

for i in range(number_of_customers) :
    temp = input().split()

    for j in range(len(temp)) :
        temp[j] = int(temp[j])
    
    demands.append(temp)

money_earned = 0

for i in range(number_of_customers) :
    if demands[i][0] in shoe_dictionary.keys() :
        if shoe_dictionary[demands[i][0]] > 0 :
            money_earned += demands[i][1]
            shoe_dictionary[demands[i][0]] = shoe_dictionary[demands[i][0]] - 1

print(money_earned)