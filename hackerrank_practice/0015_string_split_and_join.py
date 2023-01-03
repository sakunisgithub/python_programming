def split_and_join(string) :

    string = string.split()
    result = "-".join(string)
    return result

if __name__ == '__main__' :
    my_string = input()
    output = split_and_join(my_string)
    print(output)
