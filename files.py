a = 0
with open("poem.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines[0].split(" ")[2])
    for i in range(0, len(lines)):
        a += int(lines[i].split(" ")[2])
    print(a / len(lines))   

