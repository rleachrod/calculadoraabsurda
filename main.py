rango= 5000
programa = open("calculadora.py", "w")

programa.write("num1 = int(input(\"Introduce el primer numero: \"))\n")
programa.write("op=\" \"\n")
programa.write("while not(op in \"+-/*\"): \n")
programa.write("    op = input(\"Introduce el operador: \")\n")
programa.write("num2 = int(input(\"Introduce el segundo numero: \"))\n")
for index1 in range(rango):
    for index2 in range(rango):
        programa.write("if num1 == " + str(index1) + " and op == \"+\" and num2 == " + str(index2) + " :\n  print(\"" + str(index1+index2) + "\")\n")

for index1 in range(rango):
    for index2 in range(rango):
        programa.write("if num1 == " + str(index1) + " and op == \"*\" and num2 == " + str(index2) + " :\n  print(\"" + str(index1*index2) + "\")\n")

for index1 in range(rango):
    for index2 in range(rango):
        programa.write("if num1 == " + str(index1) + " and op == \"-\" and num2 == " + str(index2) + " :\n  print(\"" + str(index1-index2) + "\")\n")

for index1 in range(rango):
    for index2 in range(1,rango):
        programa.write("if num1 == " + str(index1) + " and op == \"/\" and num2 == " + str(index2) + " :\n  print(\"" + str(index1/index2) + "\")\n")

programa.write("num2 = int(input(\" \"))\n")

