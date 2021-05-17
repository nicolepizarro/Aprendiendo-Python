## Calcular el sueldo de una persona, conociendo la cantidad de horas que trabaja en el mes y el valor de la hora.

valorHora = int(input("¿Cuánto cobras por hora de trabajo? "))
horasTrabajadas = int(input("¿Cuántas horas trabajaste este mes? "))

sueldo = valorHora * horasTrabajadas 

print("Tu sueldo de este mes es " + str(sueldo))