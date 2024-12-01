def to_jaden_case(string):
    string = string.split()
    out_lst = []
    n = 0
    print(string)
    ln = len(string)

    while n < ln:
        word = string[n]
        word = word.capitalize()
        out_lst.append(word)
        n += 1

    return ' '.join(out_lst)


print(to_jaden_case("ff ff ff"))