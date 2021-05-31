
while True:
    name = input("Name: ")
    if name == '0':
        break
    else:
        diff = input("Difficulty: ")
        rune1 = input("Rune 1: ")
        rune2 = input("Rune 2: ")
        rune3 = input("Rune 3: ")
        rune4 = input("Rune 4: ")
        rune5 = input("Rune 5: ")
        rune6 = input("Rune 6: ")
        armMr = input("Armor or mr?: ")
        starting = input("Starting item: ")
        coreItems = input("Core items ")

        template = ''' %s = {
            "name": "%s",
            "diff": %s,
            "rune1": "%s",
            "rune2": "%s",
            "rune3": "%s",
            "rune4": "%s",
            "rune5": "%s",
            "rune6": "%s",
            "armMr": "%s",
            "starting": "%s",
            "coreItems": "%s",
        } ''' % (name, name, diff, rune1, rune2, rune3, rune4, rune5, rune6, armMr, starting, coreItems)
        with open("dicts.txt", "a") as dicts:
             dicts.append(template)

        