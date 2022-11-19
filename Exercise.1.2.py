#Lab  Exercise.1.2 1630902656 Kanokporn Hudsree
Run = "Fr"
totol = 9
Space = totol // 2
Star = totol % 2
mr = 2
for i in range (0,mr):
    while(Run == "Fr"):
        print((" " * Space) + ("*" * Star) + "\n")
        Space -= 1
        Star += 2
        if (Space == 0):
            Run = "Backward"
    while(Run == "Backward"):
        print((" " * Space) + ("*" * Star) + "\n")
        Space += 1
        Star -= 2
        if (Space == (totol // 2) + 1):
            Run = "Fr"
            Space = totol // 2
            Star = totol % 2
