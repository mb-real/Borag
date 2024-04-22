import sys

L = int(sys.argv[1])
R = int(sys.argv[2])

result = "1"

for item in range(17):
    for char in result:
        if char == "1":
            result += "0"
        elif char == "0":
            result += "1"

#print(len(result))
print(result[(L-1):R])
