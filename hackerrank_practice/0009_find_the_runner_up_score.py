n = int(input())

scores = [int(x) for x in input().split()]

unique_scores = []

for i in scores :
    if i not in unique_scores :
        unique_scores.append(i)

unique_scores.sort(reverse=True)

print(unique_scores[1])