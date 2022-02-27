def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_inver = palabra[::-1]

    numeros = ["0","1","2","3","4","5","6","7","8","9"]

    try:
        for index in numeros:
            if index in palabra:
                raise ValueError("Por favor ingresa una palabra, por lo menos hay un numero dentro de ella") 
        return palabra == palabra[::-1]
    
    except ValueError as ve:
        print(ve)
        return False

def run():
    palabra = input('Ingresa una palabra: ')
    es_palindromo = palindromo(palabra)
    
    if es_palindromo == True:
        print(palabra + ', es palindroma')
    else:
        print(palabra + ', NO es palindroma')


if __name__ == '__main__':
    run()