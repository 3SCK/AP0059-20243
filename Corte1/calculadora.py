# Clase Operaciones
class Operaciones:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: No se puede dividir por cero"

# Main principal
def main():
    calc = Operaciones()

    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = int(input("Selecciona una operación: "))
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        print("Resultado:", calc.suma(num1, num2))
    elif opcion == 2:
        print("Resultado:", calc.resta(num1, num2))
    elif opcion == 3:
        print("Resultado:", calc.multiplicacion(num1, num2))
    elif opcion == 4:
        print("Resultado:", calc.division(num1, num2))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
