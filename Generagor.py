import random
caracters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Ingresa la longitud de la contrasena:"))
resultado = ""

for i in range(longitud):
    resultado += random.choice(caracters)

print(f"Tu contrasena de {longitud} caracteres es: {resultado}")
