""" 5. Desarrolla un programa que permita leer 2 valores y que emita por pantalla la suma, la resta, 
el producto, la división, el resto, el promedio y el doble producto del primero menos la mitad del segundo."""
import statistics

def main():
    def suma (num1, num2):
        return num1 + num2

    def resta (num1, num2):
        return num1 - num2
    
    def producto (num1, num2):
        return num1 * num2

    def div (num1, num2):
        return num1 / num2
    
    def resto (num1, num2):
        return num1 % num2

    def prom (num1, num2):
        return statistics.mean([num1, num2])

    def doble_prod (num1, num2):
        return (num1 - 1/2 * num2) * (num1 - 1/2 * num2)

    print(f"Suma 1 + 1: {suma(1, 1)}\nResta 10 - 3: {resta(10,3)}\nProducto 2*2: {producto(2,2)}\
        \nDivision 4/2: {div(4,2)}\nResto 10/3: {resto(10,3)}\nPromedio: 1 y 5: {prom(1,5)}\
        \nDoble Producto: 1 y 4: {doble_prod(1,4)}")

if __name__ == "__main__":
    main()
