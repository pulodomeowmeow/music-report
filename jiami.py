def func(string: str):
    list = []
    list2 = []
    for i in string:
        # print(i)
        if i == " ":
            list.append(-1)
            list2.append(1)
        elif i.isalpha():
            list.append(ord(i.upper()))
            if i.islower():
                list2.append(0.5)
            else:
                list2.append(1)

    return list, list2


if __name__ == "__main__":
    list,list2 = func("Aabc d ")
    print(list)
    print(list2)
