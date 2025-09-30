def m3_13(słownik):
    return all(słownik[i] == 12 for i in słownik)

def m3_14(słownik):
    for i in poziomy.items():
        print(i)
    if isinstance(poziomy["a"], dict):
        print("!")
    return "!"

def m3_29(słowo):
    if len(słowo) <= 1:
        return słowo
    return słowo[-1] + m3_29(słowo[:-1])