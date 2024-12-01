def is_isogram(string):
    sstring = list(string)
    sstring = ''.join(map(str, sstring))
    sstring2 = set(sstring)
    sstring2 = ''.join(map(str, sstring2))
    sstring2 = sstring2.upper()
    sstring = sstring.upper()
    if sstring != sstring2:
        flag = False
    else:
        flag = True
    return flag
print(is_isogram('aba'))