def split_and_join(line):
    a=line
    b=a.split(" ")
    return "-".join(b)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
