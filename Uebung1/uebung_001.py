# Uebung 001 — Schleifen & Funktionen
# Schreibe deinen Code hier.

# Schleifen
sumTotal = 0 #Define a variable to store the sum

for i in range(437, 32483): #Range exludes the last number, so I have to make it go until 32483 instead
    sumTotal += i #Abbreviated version of writing "sumTotal = sumTotal + i"
print(sumTotal)


# Funktionen
def calcFloats(a, b):
    if a > b:
        result = b / a
        return result
    elif b > a:
        result = a / b
        return result
    else:
        result = 1
        return result
    
a = 3
b = 3

resultFloat = calcFloats(a, b)

print(resultFloat)
