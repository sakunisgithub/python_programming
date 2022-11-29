def ispossible(string, size) :

    if (size % 3 == 0) :
        code = 1
        for i in range(1, size, 3) :
            if (string[i] != string[i+1]) :
                code = 0
                break
        
        if (code) :
            return 1
        else :
            return 0
            
    elif (size % 3 == 1) :
        if size == 1 :
            return 1
        else :
            code = 1
            for i in range(1, size, 3) :
                if (string[i] != string[i+1]) :
                    code = 0
                    break

            if (code) :
                return 1
            else :
                return 0
            

    elif (size % 3 == 2) :
        return 0

            
testcases = int(input())

for i in range(testcases) :
    length = int(input())
    word = input()

    if (ispossible(word, length)) :
        print("YES")
    else : 
        print("NO")

# https://codeforces.com/problemset/problem/1765/B