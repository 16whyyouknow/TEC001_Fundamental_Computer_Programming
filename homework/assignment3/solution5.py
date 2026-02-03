def middle_char(s):
    length = len(s)
    if length == 0:
        return ""
    if length % 2 == 0:
        return s[(length // 2) - 1: (length // 2) + 1]
    else:
        return s[length // 2]

print(middle_char("python"))    # th
print(middle_char("rules"))     # l
print(middle_char("a"))         # a
print(middle_char(""))          #