from main.CoasterUtils import CoasterUtils

utils = CoasterUtils()

var = int(input("Please enter a number: "))
print("You entered " + str(var))
base = "out/"

for j in range(1, var+1):
    fh = open(base + str(j) + ".py", "w")
    for i in range(1, j+1):
        fh.write("print(\"" + str(utils.get_val(i)) + "\")\n")
    fh.close()

print("done!")
