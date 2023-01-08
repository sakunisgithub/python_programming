names = ["Yudhistir", "Arjun" , "Bheem" , "Nakul" , "Sahadeb"]

for index, name in enumerate(names) :
    print(index, name)
    if (index == 1) :
        print("Shri Krishna")

for index, name in enumerate(names, start=1) :
    print(index, name)
    if (index == 3) : # here "Bheem" is at index 3 as indexing has started from 1
        print("Astra - Gada")