testcases = int(input())

for i in range(testcases) :
    string = input()

    length = len(string)

    if (length == 1) :
        if (string[0] == 'Y' or string[0] == 'e' or string[0] == 's') :
            print("YES")
        else :
            print("NO")
    else :
        for j in range(length-1) :
            if (string[j] != 'Y' and string[j] != 'e' and string[j] != 's') :
                print("NO")
                break
            elif (string[j] == 'Y' and string[j+1] != 'e') :
                print("NO")
                break
            elif (string[j] == 'e' and string[j+1] != 's') :
                print("NO")
                break
            elif (string[j] == 's' and string[j+1] != 'Y') :
                print("NO")
                break
            
            if (j == length-2) :
                print("YES")


# https://codeforces.com/problemset/problem/1759/A