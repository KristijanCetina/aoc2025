with open("input", "r") as inputfile:
    command = [d for d in inputfile.read().strip().split("\n")]
    position = 50
    pos0 = 0
    for com in command:
        direction, value = com[0], com[1:]
        if direction == "L":
            position = (position - int(value)) % 100
            print("pozicija: ", position)
        else:
            position = (position + int(value)) % 100
            print("pozicija: ", position)
        if position == 0:
            pos0 += 1
            print("0 detected")
    print(pos0)
