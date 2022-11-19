#Lab  Exercise.1.4 1630902656 Kanokporn Hudsree
a = int(input("Enter Harmonic step: "))        
def sum(a):
    if a < 2:
        return 1
    else:
        return 1 / a + (sum(a-1))
        
for number in range(1,a+1):
    if number == number:
        print("limit = ",number,"Value = ",sum(number))
