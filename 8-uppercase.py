def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            i = chr(ord(i) - 32)
        print(i, end="")
    print()
