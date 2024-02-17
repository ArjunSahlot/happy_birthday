import sys

with open(sys.argv[1], "r") as f:
    text = f.read()
    reading = 0
    current = ""
    total = []
    for i in range(len(text)):
        reading -= 1
        if reading != 0 and text[i:i+4] == " d=\"":
            reading = 4
        if reading == 0:
            if text[i] == "\"":
                reading = 0
                total.append(current)
                current = ""
                continue
            current += text[i]
            reading = 1 

    print(total)
