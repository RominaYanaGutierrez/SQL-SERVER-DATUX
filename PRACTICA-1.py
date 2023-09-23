'''PROBLEMA 1'''
nombre = input("Bienvenido, introduce tu nombre: ")
print("¡Hola " + nombre + "!")

'''PROBLEMA 2'''
dinero = float(input("Cliente, introduzca la cantidad de su consumo (en soles): "))
propina= 0.15* dinero
print("Estimado cliente, la propina es s/." + str(propina))

'''PROBLEMA 3'''
print("BIENVENIDO")
payaso = float(input("Introduzca la cantidad de payasos: "))
peso_payasos= 112* payaso
muneca = float(input("Introduzca la cantidad de muñecas: "))
peso_muneca= 75*muneca
total=peso_muneca+peso_payasos
print("ESTIMADO CLIENTE")
print("El peso total de los payasos son " + str(peso_payasos)+" gramos")
print("El peso total de las muñecas son " + str(peso_muneca)+" gramos")
print("El paquete pesará en total " + str(total)+" gramos")

'''PROBLEMA 4'''
print("BIENVENIDO")
N = int(input("Ingrese un entero positivo: "))
suma = (N*(N+1))/2
print("La suma de todos los enteros desde 1 hasta", N, "es:", suma)

'''PROBLEMA 5'''
print("BIENVENIDO")
vistos = int(input("Ingrese cuántos shows musicales ha visto en el último año: "))

visto_mas_de_3 = vistos > 3

print("¿Ha visto más de 3 shows?:", visto_mas_de_3)

'''PROBLEMA 6'''
print("BIENVENIDO")
edad = int(input("Ingrese su edad: "))
if edad < 4:
    precio = "gratis"
elif edad >= 4 and edad <= 18:
    precio = "S/. 5"
else:
    precio = "S/. 10"
print("El precio de entrada es " + str(precio))

'''PROBLEMA 7'''
print("BIENVENIDO")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
print("Menú:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta de los dos números (el primero menos el segundo)")
print("3. Mostrar la multiplicación de los dos números")
opcion = int(input("Ingrese una opción: "))
if opcion == 1:
    resultado = numero1 + numero2
    print("La suma de los dos números es:", resultado)
elif opcion == 2:
    resultado = numero1 - numero2
    print("La resta de los dos números es:", resultado)
elif opcion == 3:
    resultado = numero1 * numero2
    print("La multiplicación de los dos números es:", resultado)
else:
    print("Opción inválida. Por favor, ingrese una opción válida.")

'''PROBLEMA 8'''
print("BIENVENIDO")
hora = input("Ingrese la hora actual en formato de 24 horas (00:00): ")
horas, minutos = hora.split(":")
hora_real = float(horas) + float(minutos) / 60
if hora_real >= 7.0 and hora_real <= 8.0:
    print("Es la hora del desayuno.")
elif hora_real >= 12.0 and hora_real <= 13.0:
    print("Es la hora del almuerzo.")
elif hora_real >= 18.0 and hora_real <= 19.0:
    print("Es la hora de la cena.")

'''PROBLEMA 9'''
lista= ['Di', 'buen', 'día', 'a', 'papa']
lista.reverse()
print(lista)

'''PROBLEMA 10'''
lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
eliminar = [0, 4, 5]
eliminar.sort(reverse=True)
for eliminacion in eliminar:
    lista.pop(eliminacion)
print(lista)

'''PROBLEMA 11'''
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_procesada = list(set(lista_original))
print(lista_procesada)

'''PROBLEMA 12'''
def obtener_tipo_mime(nombre_archivo):
    extensiones_mime = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }
    extension = nombre_archivo.lower().split('.')[-1]
    if extension in extensiones_mime:
        return extensiones_mime[extension]
    else:
        return 'application/octet-stream'
nombre_archivo = input("Nombre Archivo: ")
tipo_mime = obtener_tipo_mime(nombre_archivo)
print("Salida Esperada:", tipo_mime)
