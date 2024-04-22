
n = input()
n = n.split(" ")
L = int(n[0])
R = int(n[1])

result = "1"

for item in range(17):
    for char in result:
        if char == "1":
            result += "0"
        elif char == "0":
            result += "1"

#print(len(result))
print(result[(L-1):R])
