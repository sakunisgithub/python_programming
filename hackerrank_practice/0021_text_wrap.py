import textwrap

def wrap(string, width) :
    output = "\n".join(textwrap.wrap(string, width=width))
    return output

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)