''' dato = input('Ingrese dato: ')

lista = ['hola', 'mundo', 'chanchito', 'feliz']

if lista.count(dato) > 0:
    print('El dato existe: ', dato)
else:
    print('El dato no existe: ', dato)

'''

primero = input('Ingrese primer numero: ')
try: # try exceptm first input
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese segundo numero: ')
'''
print(primero + segundo) # concatenación
'''
'''
primerNumero = int(primero)
segundoNumero = int(segundo)
print(primerNumero + segundoNumero) # sumación
'''
try: # try except, second input
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('ingrese operación: ') # operator input

if simbolo == '+':
    print('Suma: ', primero + segundo)
elif simbolo == '-':
    print('Resta: ', primero - segundo)
elif simbolo == '*':
    print('Multiplicación: ', primero * segundo)
elif simbolo == '/':
    print('División: ', primero / segundo)
else:
    print('El símbolo ingresado no es válido')


'''
if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
    print('Ingresaste mal un dato, prueba de nuevo solo con numeros')
else:
    print(primero + segundo)
'''