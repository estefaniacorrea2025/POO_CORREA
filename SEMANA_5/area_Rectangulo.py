# Datos de entrada
base = 6                      # int
altura = 4.2                 # float
mensaje = "Iniciando el cálculo del área..."  # string
# Aquí verifico si los valores son válidos. Solo voy a continuar si ambos son mayores que cero.
es_valido = base > 0 and altura > 0

# Imprimo el mensaje para que el usuario sepa que el cálculo ha comenzado.
print(mensaje)

# Si los datos son correctos, hago el cálculo multiplicando base por altura
if es_valido:
    area = base * altura
    print("Base:", base)
    print("Altura:", altura)
    print("Área del rectángulo:", area)
    # Si los datos no son válidos, aviso al usuario con un mensaje de error.
else:
    print("Error: La base y la altura deben ser mayores que cero.")