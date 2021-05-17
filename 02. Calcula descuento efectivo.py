## 2. Calcular el importe que debe pagar una persona compra una heladera
## de pesos X y por pagar en efectivo le hacen el 10% de descuento ¿Cuánto
## abona?

valorHeladera = int(input("Ingresar valor heladera: "))

print ("Formas de pago: 1. Efectivo 2. Tarjeta")
formaPago =int(input("Elegir forma de pago: "))

if formaPago == 1:
    print ("Ha seleccionado pago en efectivo por lo que tendrá 10 de descuento")

    valorEfectivo = valorHeladera * 0.9

    print ("El total de su compra es " + str(valorEfectivo))

else:
    print ("El total de su compra es " + str (valorHeladera))
