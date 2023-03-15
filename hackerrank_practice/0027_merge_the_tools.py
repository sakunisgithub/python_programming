def make_unique_string(string) :
    print(string[0], end="")

    for i in range(1, len(string)) :
        if string[i] not in string[:i] :
            print(string[i], end="")
            
    print("\n", end="")

def merge_the_tools(string, k):

    m = int(len(string) / k)

    for i in range(m) :
        make_unique_string(string[i*k : (i*k + k)])

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)