operations = {"+","-","*","/" }
num1= int(input("enter a first number:? "))
num2 = int(input("enter second number:? "))
for symbols in operations:
 print(symbols) 
calculation_operator= input("enter the operator which you want : ")
operation= (f"{num1} {calculation_operator}{num2}")
result={operation}
print(f"answer is {result}")