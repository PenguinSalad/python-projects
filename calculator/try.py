while True:
    inp = (input(": "))
    try:
        inp = float(inp)
        inp /= 10
        break
    except ValueError:
        print("Numbers only")


print(int(inp))